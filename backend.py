import sqlite3


def create_table(): 
    connect = sqlite3.connect("dairy.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS stories (id INTEGER PRIMARY KEY, date REAL, title TEXT, note TEXT)")
    connect.commit()
    connect.close()

def insert(date, title, note):
    connect = sqlite3.connect("dairy.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO stories VALUES (NULL,?,?,?)", (date,title,note))
    connect.commit()
    connect.close()

def viewAll():
    connect = sqlite3.connect("dairy.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM stories")
    rows=cursor.fetchall()
    connect.close()
    return rows

# def delete(date, title):
#     connect = sqlite3.connect("dairy.db")
#     cursor = connect.cursor()
#     cursor.execute("DELETE FROM stories WHERE date=? AND title=?", (date,title))
#     connect.commit()
#     connect.close()

#Delete using id
def delete(id):
    connect = sqlite3.connect("dairy.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM stories WHERE id=?", (id,))
    connect.commit()
    connect.close()

# def searchAll(id = "", date = "", title =""):
#     connect = sqlite3.connect("dairy.db")
#     cursor = connect.cursor()
#     cursor.execute("SELECT * FROM stories WHERE id=? OR date=? OR title=?", (id,date,title))
#     # connect.commit()
#     searches = cursor.fetchall()
#     connect.close()
#     return searches

def searchAll(date = "", title =""):
    connect = sqlite3.connect("dairy.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM stories WHERE date=? OR title=?", (date,title))
    searches = cursor.fetchall()
    connect.close()
    return searches

create_table()

# print(viewAll())



# def searchPrint():
#     for rows in viewAll():
#         print(rows)

# searchPrint()
