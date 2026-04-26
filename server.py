# author: Gerry Callaghan

from flask import Flask, request, jsonify, redirect, url_for, abort
#from DAO import bookDAO

# this command is used to initialize a flask app called app. 
# The first argument is the name of the module or package that is being run. 
# The static_url_path and static_folder parameters are used to specify the location of static files, such as HTML, CSS, and JavaScript files, leave it blank and the program will find them itself 
# In this case, the static files are located in a folder called "staticpages" and can be accessed at the root URL ("/").
app = Flask(__name__,static_url_path="", static_folder="staticpages")

# When you are at the root URL ("/"), the function index() is called.
@app.route("/", methods=["GET"])
def index():
    return "Welcome to the REST API server!"


# To retrieve all the records on the server
@app.route("/books", methods=["GET"]) # I'm mapping the URL "/books" to the function get_all_books() and specifying that it should only respond to GET requests. When a client sends a GET request to "/books", the get_all_books() function will be called and it will return a JSON response with a message "List of books". In a real application, this function would likely query a database or some other data source to retrieve the list of books and return that data in the JSON response instead of just a message.
def get_all_books():
    return jsonify({"message": "List of books"})
    #return jsonify(bookDAO.get_all_books())
# I can use either Postman (GET request) or run the curl command: "curl http://127.0.0.1:5000/books" to test this endpoint "/books"

# To find a record by id
# curl http://127.0.0.1:5000/books/1
@app.route("/books/<int:book_id>", methods=["GET"]) # I'm mapping the URL "/books/<int:book_id>" to the function find_book_by_id() and specifying that it should only respond to GET requests. The <int:book_id> part of the URL is a variable that will be passed to the function as an argument. When a client sends a GET request to "/books/1", for example, the find_book_by_id() function will be called with book_id set to 1. In this example, the function simply returns a JSON response with a message "Details for book with ID". In a real application, this function would likely query a database or some other data source to retrieve the details for the book with the specified ID and return that data in the JSON response instead of just a message.
def find_book_by_id(book_id):
    return jsonify(f"Details for book with ID")
    #return jsonify(bookDAO.find_book_by_id(book_id))
# I can use either Postman (GET request) or run the curl command: "curl http://127.0.0.1:5000/books/1" to test this endpoint "/books"


# To create a new record on the server
@app.route("/books", methods=["POST"]) # I'm mapping the URL "/books" to the function create_book() and specifying that it should only respond to POST requests. When a client sends a POST request to "/books", the create_book() function will be called. In this example, the function retrieves the JSON data sent in the body of the request using request.json, which is expected to contain information for the new book record. The function then checks if the required fields "title", "author", and "price" are present in the JSON data. If any of these fields are missing, it returns a 403 error using abort(403). If all required fields are present, it creates a new book dictionary with the provided information and returns a JSON response indicating that the book was created along with the data that was sent in the request. In a real application, this function would likely save the new book record to a database or some other data store instead of just returning a message.
def create_book():
    jsonstring = request.json  # this is the data that is sent in the body of the request, it will be a JSON string that contains the information for the new record
    # it's possible that not all fields are provided, so we should check for that and return an error if necessary
    # perhaps put the following code in a separte function to validate the input and return an error message if any required fields are missing
    book = {}
    if "title" not in jsonstring:  # if title is missing, return a 403 error
        abort(403)
    book["title"] = jsonstring["title"]
    if "author" not in jsonstring:  # if "author" in jsonstring else abort(403)
        abort(403)
    book["author"] = jsonstring["author"]
    if "price" not in jsonstring:  # if "price" in jsonstring else abort(403)
        abort(403)
    book["price"] = jsonstring["price"]
    
    return jsonify({"message": "Book created", "data": jsonstring})
    #return jsonify(bookDAO.create_book(book))
#I can use either Postman (POST request) or run the curl command: "curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books" to test this endpoint "/books"

# To update a record on the server
@app.route("/books/<int:book_id>", methods=["PUT"]) # I'm mapping the URL "/books/<int:book_id>" to the function update_book() and specifying that it should only respond to PUT requests. The <int:book_id> part of the URL is a variable that will be passed to the function as an argument. When a client sends a PUT request to "/books/1", for example, the update_book() function will be called with book_id set to 1. In this example, the function retrieves the JSON data sent in the body of the request using request.json, which is expected to contain the updated information for the book record. The function then checks if any of the fields "title", "author", or "price" are present in the JSON data. If any of these fields are present, it adds them to a dictionary representing the updated book information. Finally, it returns a JSON response indicating that the book was updated along with the data that was sent in the request. In a real application, this function would likely update the book record in a database or some other data store instead of just returning a message.
def update_book(book_id):
    jsonstring = request.json # this is the data that is sent in the body of the request, it will be a JSON string that contains the updated information
    book = {}
    if "title" in jsonstring:
        book["title"] = jsonstring["title"]
    if "author" in jsonstring:
        book["author"] = jsonstring["author"]
    if "price" in jsonstring:
        book["price"] = jsonstring["price"]

    return f"update {id} {jsonstring}"
    #return jsonify(bookDAO.update_book(book_id, book))
#I can use either Postman (PUT request) or run the curl command: "curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books/1" to test this endpoint "/books/id"

# To delete a record from the server

@app.route("/books/<int:book_id>", methods=["DELETE"]) #I'm mapping the URL "/books/<int:book_id>" to the function delete_book() and specifying that it should only respond to DELETE requests. The <int:book_id> part of the URL is a variable that will be passed to the function as an argument. When a client sends a DELETE request to "/books/1", for example, the delete_book() function will be called with book_id set to 1. In this example, the function simply returns a string "delete". In a real application, this function would likely delete the book record with the specified ID from a database or some other data store instead of just returning a message.
def delete_book(book_id):
     
    return "delete"
    #return jsonify(bookDAO.delete_book(book_id)) 
#I can use either Postman (DELETE request) or run the curl command: "curl -X DELETE http://127.0.0.1:5000/books/1" to test this endpoint "/books/id"

@app.route("/invalid", methods=["GET"]) # I'm mapping the URL "/invalid" to the function revert_to_index() and specifying that it should only respond to GET requests. When a client sends a GET request to "/invalid", the revert_to_index() function will be called. In this example, the function uses redirect() and url_for() to redirect the user to the index (home) page when they access the /invalid endpoint. The url_for("index") function generates the URL for the index() function, which is mapped to the root URL ("/"). So when a user accesses "/invalid", they will be redirected to "/".
def revert_to_index():
    return redirect(url_for("index")) # this will redirect the user to the index (home) page when they access the /invalid endpoint

# this is to run the flask app, the debug=True parameter is used to enable debug mode, which allows for easier debugging and automatic reloading of the server when code changes are made. The host='<IP_ADDRESS>' parameter is used to specify that the server should listen on all available network interfaces, allowing it to be accessed from other devices on the same network. The port=5000 parameter specifies that the server should listen on port 5000 for incoming requests.
if __name__ == '__main__':
    #app.run(debug=True, host='<IP_ADDRESS>', port=5000)
    app.run(debug=True)
