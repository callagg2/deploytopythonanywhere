#author: Gerry Callaghan 


from urllib import response
import json
import requests


def findbyid(id):
    try:
        geturl = (url + "/" + str(id))
        response = requests.get(geturl)
        book_list = response.json()
        
        book_title = (book_list['title'])
        book_author = (book_list['author'])
        
        print_message=(f"The book with the title \"{book_title}\" written by {book_author} and with the id {id} is found.")
    except requests.RequestException:
        print_message=(f"Error occurred: Book with id {id} not found.")
    
    return print_message


def createbook(newbook):
    # add the new book
    response = requests.post(url,json=newbook)
    
    # check if the book was successfully added 
    try:
        response = requests.get(url)
        response.raise_for_status()
        new_book_list = response.json()
        for book in new_book_list:
            last_book_added = (book['title'])
        if last_book_added == newbook['title']:
            print_message =(f"{newbook['title']} by {newbook['author']} was added successfully") 
        else:
            print_message =(f"{newbook['title']} by {newbook['author']} was not added successfully")
    except requests.exceptions.RequestException as e:
        print_message =(f"Error occurred: {e}") 
    
    return print_message
    
def readbooks():
    response = requests.get(url)
    print(response.status_code) # check for status code
    return response.json()


def updatebook(id,bookdiff):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=bookdiff)
    
    # check if the update was successful 
    try:
        response = requests.get(puturl)
        response.raise_for_status()
        updated_book_list = response.json()
        print_message =(f"{updated_book_list['title']} by {updated_book_list['author']} was updated successfully") 
    except requests.exceptions.RequestException:
        print_message =(f"Error occurred: Book with id {id} not found. Update failed.") 
    
    return print_message


def deletebook(id):
    geturl = (url + "/" + str(id))
    response = requests.get(geturl)
    book_to_be_deleted = response.json()
    print(f"Book to be deleted: {book_to_be_deleted}")
    
    # Now we delete that book
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)

    # check if the delete was successful (gemini helped here https://gemini.google.com/share/1e0dfbb28400)
    try:
        geturl = (url + "/" + str(id))
        response = requests.get(geturl)
        response.raise_for_status()
        print_message =(f"{book_to_be_deleted} was not deleted successfully") 
    except requests.exceptions.RequestException as e:
        print_message =(f"{book_to_be_deleted} was deleted successfully") 
    
    return print_message    


if __name__ == "__main__":

    url = "https://andrewbeatty1.pythonanywhere.com/books"
    id = 1728
    newbook = {
        'author': 'Joe Smith', 
        'id': 1677, 
        'price': 20, 
        'title': 'New Book'
        }
    bookdiff = {
        'author': 'Mary-Jane Doe', 
        'price': 14, 
        'title': 'Yet Another Book'
        }

    #print(readbooks())
    #print(createbook(newbook))
    #print(findbyid(id))
    #print(updatebook(id, bookdiff))
    #print(deletebook(id))

