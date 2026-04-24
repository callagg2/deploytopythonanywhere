# author: Gerry Callaghan

from flask import Flask, request, jsonify, redirect, url_for, abort
from DAO import bookDAO

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
@app.route("/books", methods=["GET"])
def get_all_books():
    #return jsonify({"message": "List of books"})
    return jsonify(bookDAO.get_all_books())
# I can use either Postman (GET request) or run the curl command: "curl http://127.0.0.1:5000/books" to test this endpoint "/books"

# To find a record by id
# curl http://127.0.0.1:5000/books/1
@app.route("/books/<int:book_id>", methods=["GET"])
def find_book_by_id(book_id):
    #return jsonify(f"Details for book with ID")
    return jsonify(bookDAO.find_book_by_id(book_id))
# I can use either Postman (GET request) or run the curl command: "curl http://127.0.0.1:5000/books/1" to test this endpoint "/books"


# To create a new record on the server
@app.route("/books", methods=["POST"])
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
    
    #return jsonify({"message": "Book created", "data": jsonstring})
    return jsonify(bookDAO.create_book(book))
#I can use either Postman (POST request) or run the curl command: "curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books" to test this endpoint "/books"

# To update a record on the server
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    jsonstring = request.json # this is the data that is sent in the body of the request, it will be a JSON string that contains the updated information
    book = {}
    if "title" in jsonstring:
        book["title"] = jsonstring["title"]
    if "author" in jsonstring:
        book["author"] = jsonstring["author"]
    if "price" in jsonstring:
        book["price"] = jsonstring["price"]

    #return f"update {id} {jsonstring}"
    return jsonify(bookDAO.update_book(book_id, book))
#I can use either Postman (PUT request) or run the curl command: "curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books/1" to test this endpoint "/books/id"

# To delete a record from the server

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
     
    #return "delete"
    return jsonify(bookDAO.delete_book(book_id)) 
#I can use either Postman (DELETE request) or run the curl command: "curl -X DELETE http://127.0.0.1:5000/books/1" to test this endpoint "/books/id"

@app.route("/invalid", methods=["GET"])
def index():
    return redirect(url_for("index")) # this will redirect the user to the index (home) page when they access the /invalid endpoint

# this is to run the flask app, the debug=True parameter is used to enable debug mode, which allows for easier debugging and automatic reloading of the server when code changes are made. The host='<IP_ADDRESS>' parameter is used to specify that the server should listen on all available network interfaces, allowing it to be accessed from other devices on the same network. The port=5000 parameter specifies that the server should listen on port 5000 for incoming requests.
if __name__ == '__main__':
    #app.run(debug=True, host='<IP_ADDRESS>', port=5000)
    app.run(debug=True)
