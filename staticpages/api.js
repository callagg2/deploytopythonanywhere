const url = "/books";
let books = [];

function getBookItems() {
  fetch(url)
    .then(response => response.json())
    .then(data => _displayItems(data))
    .catch(error => console.error("Unable to get books.", error));
}

function getOneBookItem() {
  const id = document.getElementById("search-id").value.trim();

  fetch(`${url}/${id}`)
    .then(response => {
      if (!response.ok) {
        throw new Error("Book not found");
      }
      return response.json();
    })
    .then(data => {
      _displayItems([data]); // show the book found
       $('#searchBookModal').modal('hide');   // auto-close the modal
    })
    .catch(error => console.error("Unable to find that book.", error));

  return false; // prevent form reload
}

function findBookForm(id) {
  const item = books.find(item => item.id === id);
  document.getElementById("find-id").value = item.id;
}

$('#searchBookModal').on('show.bs.modal', function () {
  document.getElementById("search-id").value = "";
});


function _displayfindbook(data) {

  data.forEach(item => {
    let searchButton = document.createElement("a"); // create a button element to be used for the search button in the table
    searchButton.href = "#findBookModal"; // set the href attribute of the search button to the id of the modal that will be used to display the search results
    searchButton.className = "search"; // set the class name of the search button to "search" for styling purposes
    searchButton.setAttribute("onclick", `findBookForm(${item.id})`); // set the onclick attribute of the search button to call the findBookForm function with the id of the book item as an argument when the button is clicked
    searchButton.setAttribute("data-toggle", "modal"); // set the data-toggle attribute of the search button to "modal" to enable the modal functionality
    searchButton.innerHTML =
      "<i class='material-icons' data-toggle='tooltip' title='Search'>&#xE8B6;</i>";
  });
}

function addBookItem() {
  /*const idInputText = document.getElementById("add-ID");*/
  const titleInputText = document.getElementById("add-title");
  const authorInputText = document.getElementById("add-author");
  const publisherInputText = document.getElementById("add-publisher");
  const priceInputText = document.getElementById("add-price");

$('#addBookModal').on('show.bs.modal', function () {
  /*document.getElementById("add-ID").value = "";*/
  document.getElementById("add-title").value = "";
  document.getElementById("add-author").value = "";
  document.getElementById("add-publisher").value = "";
  document.getElementById("add-price").value = "";
});

  const item = {
    /*id: parseInt(idInputText.value.trim()),*/
    title: `<a href="${titleInputText.value.trim()}">${titleInputText.value.trim()}</a>`,
    author: authorInputText.value.trim(),
    publisher: publisherInputText.value.trim(),
    price: parseInt(priceInputText.value.trim())
  };
  console.log(JSON.stringify(item));
  fetch(url, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    body: JSON.stringify(item)
  })
    .then(response => response.json())
    .then(() => {
      getBookItems();
      /*idInputText.value = "";*/
      titleInputText.value = "";
      authorInputText.value = "";
      publisherInputText.value = "";
      priceInputText.value = "";
    })
    .catch(error => console.error("Unable to add Book.", error));
}


function deleteBookItem() {
  const itemId = document.getElementById("delete-id").value.trim();
  fetch(`${url}/${itemId}`, {
    method: "DELETE"
  })
    .then(() => getBookItems())
    .catch(error => console.error("Unable to delete Book.", error));
}

function displayDeleteForm(id) {
  const item = books.find(item => item.id === id);
  document.getElementById("delete-id").value = item.id;
}

function displayEditForm(id) {
  const item = books.find(item => item.id === id);
  document.getElementById("edit-id").value = item.id;
  document.getElementById("edit-title").value = item.title;
  document.getElementById("edit-author").value = item.author;
  document.getElementById("edit-publisher").value = item.publisher;
  document.getElementById("edit-price").value = item.price;
}

function updateBookItem() {
  const itemId = document.getElementById("edit-id").value.trim();
  const item = {
    /*id: parseInt(itemId, 10),*/
    id: parseInt(document.getElementById("edit-id").value.trim()),
    title: document.getElementById("edit-title").value.trim(),
    author: document.getElementById("edit-author").value.trim(),
    publisher: document.getElementById("edit-publisher").value.trim(),
    price: parseInt(document.getElementById("edit-price").value.trim())
  };

  fetch(`${url}/${itemId}`, {
    method: "PUT",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    body: JSON.stringify(item)
  })
    .then(() => getBookItems())
    .catch(error => console.error("Unable to update item.", error));

  return false;
}

function _displayCount(itemCount) {
  const name = itemCount === 1 ? "entry" : "entries";
  document.getElementById(
    "counter"
  ).innerHTML = `Showing <b>${itemCount}</b> ${name}`;
}

function _displayItems(data) {
  const tBody = document.getElementById("books"); // get the table body element by its id
  tBody.innerHTML = "";
  _displayCount(data.length); // display the number of book items in the table
  const button = document.createElement("button"); // create a button element to be used for the edit and delete buttons in the table

  data.forEach(item => {
    let editButton = document.createElement("a");
    editButton.href = "#editBookModal";
    editButton.className = "edit";
    editButton.setAttribute("onclick", `displayEditForm(${item.id})`);
    editButton.setAttribute("data-toggle", "modal");
    editButton.innerHTML =
      "<i class='material-icons' data-toggle='tooltip' title='Edit'>&#xE254;</i>";

    let deleteButton = document.createElement("a");
    deleteButton.href = "#deleteBookModal";
    deleteButton.className = "delete";
    deleteButton.setAttribute("onclick", `displayDeleteForm(${item.id})`);
    deleteButton.setAttribute("data-toggle", "modal");
    deleteButton.innerHTML =
      "<i class='material-icons' data-toggle='tooltip' title='Delete'>&#xE872;</i>";

    // each tr is a row in the table, so we insert a new row for each book item    
    let tr = tBody.insertRow();
    // each td is a column in the table, so we insert 6 columns for each book item
    let td1 = tr.insertCell(0);
    let textid = document.createTextNode(item.id);
    td1.appendChild(textid); // add the book id to the first column of the table

    let td2 = tr.insertCell(1);
    //let textTitle = document.createTextNode(item.title);
    //td2.appendChild(textTitle); // add the book title to the second column of the table
      td2.innerHTML = item.title; // add the book title to the second column of the table, using innerHTML to render the link

    let td3 = tr.insertCell(2);
    let textAuthor = document.createTextNode(item.author);
    td3.appendChild(textAuthor); // add the book author to the third column of the table

    let td4 = tr.insertCell(3);
    let textPublisher = document.createTextNode(item.publisher);
    td4.appendChild(textPublisher); // add the book publisher to the fourth column of the table

    let td5 = tr.insertCell(4);
    let textPrice = document.createTextNode(item.price);
    td5.appendChild(textPrice); // add the book price to the fifth column of the table

    let td6 = tr.insertCell(5);
    td6.appendChild(editButton);
    td6.appendChild(deleteButton);
  });

  books = data;
}