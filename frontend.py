from tkinter import *

import backend

window = Tk()
window.wm_title("MyDairy")
# window.geometry("450x570")

#Commands
#Resizing window automatically
def on_resize(event):
    viewNote_width = event.width
    viewNote_height = event.height
    viewNote.config(viewNote_width, viewNote_height)

def viewNoteCommand():
    global viewNote
    viewNote = Toplevel(window)
    viewNote.wm_title("MyDiary")
    viewNote.bind("<<Configure>>", on_resize)

    t9 = Text(viewNote, height = 40, width = 80)
    t9.pack()
    t9.insert(END, note)

    button = Button(viewNote, text="Close", command=closeCommand2)
    button.pack()
    
def viewCommand():
    global rows     #used because of the insert method in the deleteCommand() function
    list1.delete(0, END)
    for rows in backend.viewAll():
        list1.insert(END, rows)

def searchCommand():
    list1.delete(0, END)
    for searches in backend.searchAll(e1_entry.get(), e2_entry.get()):
        list1.insert(END, searches)

def enterCommand():
    backend.insert(e1_entry.get(), e2_entry.get(), t1.get('1.0', 'end-1c'))
    list1.delete(0, END)
    list1.insert(END, (e1_entry.get(), e2_entry.get(), t1.get('1.0', 'end-1c')), "New dairy story added!")
    t1.delete(1.0, END)
    
def closeCommand():
    window.destroy()
    
def closeCommand2():
    viewNote.destroy()

def selectedRow(event):
    index = list1.curselection()[0]
    global row
    global note
    row = list1.get(index)
    note = list1.get(index)[3]
    # print(index)
    # print(note)
    # print(row)

def deleteCommand():
    backend.delete(row[0])
    list1.delete(0, END)
    list1.insert(END,rows, "Selected story deleted!")

#Label
l1 = Label(window, text = "DAIRY GUI BY BLAZE!")
l1.grid(row=0, column=3)

l2 = Label(window, text = "Date: ")
l2.grid(row=1, column=1)

l3 = Label(window, text = "Title: ")
l3.grid(row=1, column=3)

l2 = Label(window, text = "Note for today: ")
l2.grid(row=2, column=3)

l3 = Label(window, text = "Archive: ")
l3.grid(row=7, column=0)

#entrybox
e1_entry = StringVar() 
e1 = Entry(window, textvariable = e1_entry)     #for date
e1.grid(row=1, column=2)

e2_entry = StringVar()
e2 = Entry(window, textvariable = e2_entry)     #for title
e2.grid(row=1, column=4)

#Textbox
t1=Text(window, width=50, height = 20)
t1.grid(row=4, column=0, columnspan=8)

#Button
b1 = Button(window, text = "Enter", command=enterCommand)
b1.grid(row=5, column=3, columnspan=4)

b2 = Button(window, text = "View All Notes", command=viewCommand)
b2.grid(row=8, column=3, columnspan=4)

b6 = Button(window, text = "View Note", command=viewNoteCommand)
b6.grid(row=9, column=3, columnspan=4)

b3 = Button(window, text = "Search Notes", command=searchCommand)
b3.grid(row=10, column=3, columnspan=4)

b4 = Button(window, text = "Delete Note", command=deleteCommand)
b4.grid(row=11, column=3, columnspan=4)

b5 = Button(window, text = "Close Diary", command=closeCommand)
b5.grid(row=12, column=3, columnspan=4)

#Listbox
list1 = Listbox(window, height=6, width=35)
list1.grid(row=8, column=0, rowspan=6, columnspan=3)

#Scrollbar
s1 = Scrollbar(window)
s1.grid(row=8, column=2, rowspan=10, columnspan=3)

#Configuration of Listbox and Scrollbar
list1.configure(yscrollcommand=s1.set)
s1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', selectedRow)

window.mainloop()













#VERSION 1.0
# from tkinter import *

# window = Tk()

# #Label
# l1 = Label(window, text = "DAIRY GUI BY BLAZE!")
# l1.grid(row=0, column=3)

# l2 = Label(window, text = "Date: ")
# l2.grid(row=1, column=1)

# l3 = Label(window, text = "Title: ")
# l3.grid(row=1, column=3)

# l2 = Label(window, text = "Note for today: ")
# l2.grid(row=2, column=3)

# #entrybox
# e1_entry = StringVar()
# e1 = Entry(window, textvariable = e1_entry)
# e1.grid(row=1, column=2)

# e2_entry = StringVar()
# e2 = Entry(window, textvariable = e2_entry)
# e2.grid(row=1, column=4)

# t1=Text(window, width=50, height = 20)
# t1.grid(row=4, column=0, columnspan=8)

# #Button
# b1 = Button(window, text = "Enter")
# b1.grid(row=5, column=3)

# b2 = Button(window, text = "View All Notes")
# b2.grid(row=6, column=2)

# b3 = Button(window, text = "Search Notes")
# b3.grid(row=6, column=3)

# b4 = Button(window, text = "Delete Note")
# b4.grid(row=6, column=4)

# b5 = Button(window, text = "Close GUI")
# b5.grid(row=7, column=3)


# #Listbox
# list1 = Listbox(window, height=6, width=35)
# list1.grid(row=8, column=2, rowspan=6, columnspan=4)

# window.mainloop()