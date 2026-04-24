# author: Gerry Callaghan

from flask import Flask, request, jsonify, redirect, url_for, abort
from DAOfordatabase import bookDAO

app = Flask(__name__,static_url_path="", static_folder="staticpages")

@app.route("/", methods=["GET"])
def index():
    return "Welcome to the REST API server!"

# put in explanation of jsonstring and how to use it in postman/curl
# getall
# curl http://127.0.0.1:5000/books
@app.route("/books", methods=["GET"])
def get_all_books():
    #return jsonify({"message": "List of books"})
    return jsonify(bookDAO.get_all_books())

# put in explanation of jsonstring and how to use it in postman/curl
# find by id
# curl http://127.0.0.1:5000/books/1
@app.route("/books/<int:book_id>", methods=["GET"])
def find_book_by_id(book_id):
    #return jsonify(f"Details for book with ID")
    return jsonify(bookDAO.find_book_by_id(book_id))

# put in explanation of jsonstring and how to use it in postman/curl
#create
#curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books
@app.route("/books", methods=["POST"])
def create_book():
    jsonstring = request.json 
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

# put in explanation of jsonstring and how to use it in postman/curl
# update
# curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    jsonstring = request.json
    book = {}
    if "title" in jsonstring:
        book["title"] = jsonstring["title"]
    if "author" in jsonstring:
        book["author"] = jsonstring["author"]
    if "price" in jsonstring:
        book["price"] = jsonstring["price"]

    #return f"update {id} {jsonstring}"
    return jsonify(bookDAO.update_book(book_id, book))

# put in explanation of jsonstring and how to use it in postman/curl
#delete
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
     
    #return "delete"
     return jsonify(bookDAO.delete_book(book_id)) 


if __name__ == '__main__':
    #app.run(debug=True, host='<IP_ADDRESS>', port=5000)
    app.run(debug=True)