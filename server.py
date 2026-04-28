# author: Gerry Callaghan

from flask import Flask, request, jsonify, redirect, url_for, abort 
from DAO import bookDAO

    # this command is used to initialize a flask app called app. 
    # The first argument is the name of the module or package that is being run, I've just left it as the default. 
    # The static_url_path is used to specify the URL path that will be used to access static files, 
    # I'm leaving it blank and the program will find them itself 
    # The the static files such as the HTML, CSS, and JavaScript files used for the front end 
    # are in a folder called "staticpages" and can be accessed at the root URL ("/").
app = Flask(__name__,static_url_path="", static_folder="staticpages")

    # When you are at the root URL ("/"), the function index() is called.
@app.route("/", methods=["GET"]) # this is just some onscreen message that is used to map the URL "/" to the function index() and specify that it should only respond to GET requests.
def index():
    return "Welcome to the REST API server!"


    # To retrieve or get all the records on the server
@app.route("/books", methods=["GET"]) # I'm mapping the URL "/books" to the function get_all_books() and specifying that it should only respond to GET requests. 
    # When a client sends a GET request to "/books", the get_all_books() function queries a database to retrieve the list of books 
    # and returns that data in the JSON response.
def get_all_books():
    #return jsonify({"message": "List of books"}) # used only for testing the endpoint
    # I can use either Postman (GET request) or run the curl command: "curl http://127.0.0.1:5000/books" to test this endpoint "/books"
    return jsonify(bookDAO.get_all_books())


    # To find a specific record by passing in its id
@app.route("/books/<int:id>", methods=["GET"]) # I'm mapping the URL "/books/<int:id>" to the function find_book_by_id() 
    # and specifying that it should only respond to GET requests. The <int:id> part of the URL is a variable that will be passed to the function as an argument. 
    # When a client sends a GET request to "/books/1", for example, 
    # the find_book_by_id() function will be called with id set to 1. 
    # Here, the function queries the database and retrieves the details for the book with the specified ID and return that data in the JSON response.
def find_book_by_id(id):
    #return jsonify(f"Details for book with ID {id}") # used only for testing the endpoint
    # I can use either Postman (GET request) or run the curl command: "curl http://127.0.0.1:5000/books/1" to test this endpoint "/books"

    book = jsonify(bookDAO.find_book_by_id(id)) # this will call the find_book_by_id() function
    if book:
        return book
    else:
        return jsonify({"message": f"Book with ID {id} not found"}), 404 # this will return a JSON response with a message indicating that the book was not found, and a 404 status code to indicate that the resource was not found.   


    # To create a new record on the server
@app.route("/books", methods=["POST"]) # I'm mapping the URL "/books" to the function create_book() 
    #and specifying that it should only respond to POST requests. 
def create_book():
    jsonstring = request.json  # this is the data that is to be sent up to my server in the body of the request, 
    # it will be a JSON string contains the information for the new record
    
    # Because it's possible that not all fields are provided, I'm checking for that and return an error if necessary
    # perhaps put the following code in a separate function to validate the input and return an error message if any required fields are missing
    # here is a list of error codes: - https://www.w3schools.com/tags/ref_httpmessages.asp
    # I've gone for 409 Conflict 	The request could not be completed because of a conflict in the request, insuficient data, or a logical error. 
    # This code is used in situations where the user might be able to resolve the conflict and resubmit the request. 
    book = {}
    if "title" not in jsonstring:  # if title is missing, return a 409 error
        abort(409)
    book["title"] = jsonstring["title"]
    if "author" not in jsonstring:  # if "author" in jsonstring else abort(409)
        abort(409)
    book["author"] = jsonstring["author"]
    if "price" not in jsonstring:  # if "price" in jsonstring else abort(409)
        abort(409)
    book["price"] = jsonstring["price"]
    
    #return jsonify({"message": "Book created", "data": jsonstring})
    # I can use either Postman (POST request) or run the curl command: "curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books" to test this endpoint "/books"

    return jsonify(bookDAO.create_book(book))

    # To update a record on the server
@app.route("/books/<int:id>", methods=["PUT"]) # I'm mapping the URL "/books/<int:id>" to the function update_book() 
    # and specifying that it should only respond to PUT requests. The <int:id> part of the URL is a variable that will be passed to the function as an argument. 
    # When a client sends a PUT request to "/books/1", the update_book() function will be called with id set to 1. 
def update_book(id):
    jsonstring = request.json # this is the data that is sent in the body of the request, it will be a JSON string that contains the updated information
    book = {}
    if "title" in jsonstring:
        book["title"] = jsonstring["title"]
    if "author" in jsonstring:
        book["author"] = jsonstring["author"]
    if "price" in jsonstring:
        book["price"] = jsonstring["price"]

    #return f"update {id} {jsonstring}"
    #I can use either Postman (PUT request) or run the curl command: "curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books/1" to test this endpoint "/books/id"

    return jsonify(bookDAO.update_book(id, book))

    # To delete a record from the server
@app.route("/books/<int:id>", methods=["DELETE"]) #I'm mapping the URL "/books/<int:id>" to the function delete_book() 
    #and specifying that it should only respond to DELETE requests. The <int:id> part of the URL is a variable that will be passed to the function as an argument. 
    # When a client sends a DELETE request to "/books/1", for example, the delete_book() function will be called with book_id set to 1. 
def delete_book(id):
     
    #return "delete"
    # I can use either Postman (DELETE request) or run the curl command: "curl -X DELETE http://127.0.0.1:5000/books/1" to test this endpoint "/books/id"

    return jsonify(bookDAO.delete_book(id)) 


@app.route("/invalid", methods=["GET"]) # I'm mapping the URL "/invalid" to the function revert_to_index() and specifying that it should only respond to GET requests. 
    # When a client sends a GET request to "/invalid", the revert_to_index() function will be called. 
    # In this example, the function uses redirect() and url_for() to redirect the user to the index (home) page when they access the /invalid endpoint. 
    # The url_for("index") function generates the URL for the index() function, which is mapped to the root URL ("/"). So when a user accesses "/invalid", they will be redirected to "/".
def revert_to_index():
    return redirect(url_for("index")) # this will redirect the user to the index (home) page when they access the /invalid endpoint


# this is to run the flask app, the debug=True parameter is used to enable debug mode, 
# which allows for easier debugging and automatic reloading of the server when code changes are made. 
if __name__ == '__main__':
    app.run(debug=True)
