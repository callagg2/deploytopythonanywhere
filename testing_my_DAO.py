
# author: gerry Callaghan

from DAO import bookDAO
import mysql.connector
from testing_dbconfig import config_details

book = {
    "id":"1",
    "title": "test",
    "author": "some guy",
    "price": 123    
}


# To test the create_book() function, we can run the following code:
book = bookDAO.create_book(book)
bookid = book["id"] # this is the id of the newly created book record, which I can use to test the other functions that require an id as an argument

# To test the get_all_books() function, we can run the following code:
books = bookDAO.get_all_books()
print(f"\ntest get all books:", books) # returns a list of dict objects, each dict represents a book record in the database, with the keys being the column names and the values being the corresponding values for that record.

# To test the find_book_by_id() function, we can run the following code:
result= bookDAO.find_book_by_id(bookid)
print(f"\ntest create and find by id:", book) # returns a dict object representing the book record with the specified id in the bookid = book["id"] above, with the keys being the column names and the values being the corresponding values for that record.

# To test the update_book() function, we can run the following code:
updated_book = {   
    "title": "updated test",
    "author": "some other guy",
    "price": 456 
    }            
result = bookDAO.update_book(bookid, updated_book)
original_book = result[1] # we can return the book before it was updated
#print(f"\ntest update book: 1 record updated, ID: {bookid}, Title: {result['title']}, Author: {result['author']}, Price: {result['price']}", result) # returns a dict object representing the updated book record, with the keys being the column names and the values being the corresponding values for that record. The id key will still be the same as the original book, but the other keys will have the updated values.
print(f"\ntest update book: 1 record updated", "\noriginal book:", original_book, "\nupdated book:", result[0]) # returns a dict object representing the updated book record, with the keys being the column names and the values being the corresponding values for that record. The id key will still be the same as the original book, but the other keys will have the updated values.

# To test the delete_book() function, we can run the following code:
result = bookDAO.delete_book(bookid)
book_to_be_deleted= result[1] # we can return the book that was just deleted, so that we can see what was deleted in the test output
print(f"\ntest delete book: 1 record deleted", book_to_be_deleted, ", Deleted:", result[0]) # returns a boolean value indicating whether the delete operation was successful or not. If the book with the specified id was successfully deleted, it will return True, otherwise it will return False.


    