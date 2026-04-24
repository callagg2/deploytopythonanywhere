# a simple DAO for a database that does CRUD operations on a books table
#author: Gerry Callaghan

import mysql.connector
from dbconfig import config_details

class BookDAO:

    host = config_details['host']
    user = config_details['user']
    password = config_details['password']
    database = config_details['database']
    connection = ""
    cursor = ""


    def get_cursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_all(self):
        self.cursor.close()
        self.connection.close()

    # creating data in a database
    def create_book(self, book):
        mycursor = self.get_cursor()
        sql = "Insert into books1 (title, author, price) values (%s, %s,%s)"
        values = (book.get("title"), book.get("author"), book.get("price")) # get these out of the dictionary objects, if not set, get will return None
        mycursor.execute(sql, values)

        self.connection.commit()
        print("1 record inserted, ID:", mycursor.lastrowid)
        book["id"] = mycursor.lastrowid
        self.close_all()
        return book

    # reading data from a database
    def get_all_books(self):
        mycursor = self.get_cursor()
        sql = "Select * from books1"
        mycursor.execute(sql)

        results = mycursor.fetchall()
        book_list = []
        for result in results:
            book_list.append(self.convert_to_dict(result))

        self.close_all()
        return book_list

    # finding one book by id
    def find_book_by_id(self, id):
        mycursor = self.get_cursor()
        sql = "Select * from books1 where id = %s"
        values = (id,)

        mycursor.execute(sql, values)
        results = mycursor.fetchone()
        #print(results)

        self.close_all()
        return self.convert_to_dict(results)

    # updating data in a database
    def update_book(self, bookid, book):
        mycursor = self.get_cursor()
        sql = "Update books1 set title = %s, author = %s, price = %s where id = %s"
        values = (book.get("title"), book.get("author"), book.get("price"),bookid) # get these out of the dictionary objects, if not set, get will return None
        mycursor.execute(sql, values)
        self.connection.commit()

        print("1 record updated, ID:", mycursor.lastrowid)
        self.close_all()
        return book

    # deleting data from a database
    def delete_book(self, id):
        mycursor = self.get_cursor()
        sql = "Delete from books1 where id = %s"
        values = (id,)
        mycursor.execute(sql, values)
        self.connection.commit()

        print("1 record deleted")
        self.close_all()
        return True

    def convert_to_dict(self, resultline):
        bookkeys = ["id", "title", "author", "price"]
        current_key = 0
        book = {}
        for attrib in resultline:
            book[bookkeys[current_key]] = attrib
            current_key += 1
        return book
        

bookDAO = BookDAO() # make an instance of the DAO class to use in testing



book = {"id":1,"title":"blah","author":"someone","price":999} 
#print ("test getall")
#print (f"\t{bookDAO.getAll()}")
#print ("test findById(1)")
#print (f"\t{bookDAO.findByID(1)}")
print ("test create")
print (f"\t{bookDAO.create_book(book)}")
#print ("test update")
#print (f"\t{bookDAO.update(1,book)}")
#print ("test delete")
#print (f"\t{bookDAO.delete(1)}")