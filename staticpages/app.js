function loadBooks() {
    $.ajax({
        url: `${API_URL}/books`,
        method: "GET",
        success: function (response) {
            console.log("GET /books response:", response);

            let books = [];

            // Case 1: API returns an array
            if (Array.isArray(response)) {
                books = response;
            }

            // Case 2: API returns { books: [...] }
            else if (response && Array.isArray(response.books)) {
                books = response.books;
            }

            // Case 3: API returns a single object
            else if (response && typeof response === "object") {
                books = [response];
            }

            const tbody = $("#booksTable tbody");
            tbody.empty();

            books.forEach(book => {
                tbody.append(`
                    <tr>
                        <td>${book.id}</td>
                        <td>${book.title}</td>
                        <td>${book.author}</td>
                        <td>${book.year}</td>
                        <td>
                            <button class="btn btn-warning btn-sm me-2" onclick="loadIntoForm('${book.id}')">Load</button>
                            <button class="btn btn-danger btn-sm" onclick="deleteBook('${book.id}')">Delete</button>
                        </td>
                    </tr>
                `);
            });
        },
        error: function (xhr) {
            console.error("Error loading books:", xhr.responseText || xhr.statusText);
        }
    });
}