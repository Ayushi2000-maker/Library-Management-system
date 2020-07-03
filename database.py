import sqlite3 #this is name of Database
def connect():
	'''creating a database'''
	c=sqlite3.connect('books.db') # It creates the database file named books.db  where content is stored
	cur=c.cursor() # To execute the Sqlite3 statements we need a cousor object.

	cur.execute("CREATE TABLE IF NOT EXISTS "
                    "books (id integer PRIMARY KEY, "
                            "title text, "
                            "author text, "
                            "year integer, "
                            "isbn integer)")
    
	c.commit()
	c.close()
def insert(title,author,year,isbn):
	c=sqlite3.connect('books.db')
	cur=c.cursor()
	cur.execute("INSERT INTO books "
                    "VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
	c.commit()
	c.close()
def view():
	'''view entries'''
	c=sqlite3.connect('books.db')
	cur=c.cursor()
	cur.execute("select * from books")
	rows=cur.fetchall()
	c.close()
	return rows
def update(id,title,author,year,isbn):
	c=sqlite3.connect('books.db')
	cur=c.cursor()
	cur.execute("UPDATE books "
                    "SET title = ?, "
                    "author = ?, "
                    "year = ?, "
                    "isbn = ? "
                    "WHERE id = ?", 
                    (title, author, year, isbn, id))
	c.commit()
	c.close()
def delete(d):
	''' delete entries from database'''
	c=sqlite3.connect('books.db')
	cur=c.cursor()
	cur.execute("delete from books where id=?",(d,))
	c.commit()
	c.close()
def search(title = "", author = "", year = "", isbn = ""):
    """Search for a database entry."""
    c = sqlite3.connect("books.db")
    cur = c.cursor()
    cur.execute("SELECT * "
                    "FROM books "
                    "WHERE title = ? OR author = ? OR year = ? OR isbn = ?", 
                    (title, author, year, isbn))
    rows = cur.fetchall()
    c.close()
    return rows
    
connect()

		     
