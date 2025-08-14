
class Book():
    def __init__(self, title : str, author : str, isbn : str): # type hint is written
        self.title = title
        self.author = author
        self.isbn = isbn # unique identifier

    def __str__(self) -> str :
        # Human readable representation
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    
# Inheritance
class EBook(Book):
    def __init__(self, title : str, author : str, isbn : str, file_size_mb : float):
        super().__init__(title, author, isbn) # calling parent class constructor for shared attributes
        self.file_size_mb = file_size_mb

    def __str__(self) -> str:
         # Override the parent string to include ebook info
        return f"{self.title} by {self.author} (E-Book, {self.file_size_mb} MB, ISBN: {self.isbn})"
    
# Another sub class which adds the pages
class PrintedBook(Book):
    def __init__(self, title : str, author :str, isbn: str, pages : int):
        super().__init__(title, author, isbn)
        self.pages = pages
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.pages} pages, ISBN: {self.isbn})"

# Library container
class Library():
    def __init__(self):
        # # Store Book/EBook/PrintedBook objects in a list
        self.books = []

    def add_book(self, book: Book) -> None: # Here, None is written to indicate that this function does not return anything.
        for b in self.books:
            if b.isbn == book.isbn:
                print(f"A book with ISBN {book.isbn} already exists: {b}")
                return
        self.books.append(book)
        print(f"Added {book}")

    def remove_book(self, isbn : str) :
        for b in self.books:
            if b.isbn == isbn:
                self.books.remove(b)
                print(f"Remove {b}")
                return
        print(f"Book with ISBN {isbn} not found")

    def search_book(self, query : str, by : str = "title"):
        """
        Search books by title (default), author, or isbn.
        Returns a list of matching Book objects.
        """

        query_lower = query.lower()

        if by == "title" :
            return [b for b in self.books if query_lower in b.title.lower()]
        elif by == "author":
            return [b for b in self.books if query_lower in b.author.lower()]
        elif by == "isbn":
            # Exact match for ISBN is typical
            return [b for b in self.books if b.isbn == query]
        else:
            raise ValueError("by must be one of: 'title', 'author', 'isbn'")
        
    def view_books (self) :
        if not self.books:
            print("No books available")
            return
        print("\nCurrent books :")
        for book in self.books:
            print(f"  -{book}")
    
# Example usage
if __name__ == "__main__":
    library = Library()

    while True :
        print("Library ")
        print("1. Add Printed Book")
        print("2. Add E-Book")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. View All Books")
        print("6. Exit")

        choice = int(input("Enter (1-6) : ")) # strip method removes leading and trailing white spaces

        match choice :
            case 1:
                title = input("Enter title : ")
                author = input("Enter author : ")
                isbn = input("Enter ISBN : ")
                pages = int(input("Enter number of pages : "))
                library.add_book(PrintedBook(title, author, isbn, pages))
            
            case 2 : 
                title = input("Enter title : ")
                author = input("Enter author : ")
                isbn = input("Enter ISBN : ")
                file_size_mb = float(input("Enter file size in mb : "))
                library.add_book(EBook(title, author, isbn, file_size_mb))

            case 3 :
                isbn = input("Enter ISBN to remove : ")
                library.remove_book(isbn)

            case 4 :
                search_type = input("Search by (title/author/isbn) : ").lower()
                query = input("Enter search query : ")
                results = library.search_book(query, by = search_type)
                if results:
                    print("\nSearch result : ")
                    for book in results:
                        print(f"  -{book}")
                else :
                    print("No matching books found")

            case 5 :
                library.view_books()
            
            case 6 :
                print("\nExiting loops...")
                break

            case _:
                print("Invalid input. Please try again.")
    # b1 = PrintedBook("The Great Gatsby", "F. Scott Fitzgerald", "12345", pages=180)
    # b2 = EBook("Python Programming", "John Doe", "67890", file_size_mb=5.2)
    # b3 = EBook("Effective Python", "Brett Slatkin", "11111", file_size_mb=3.8)
    # b4 = PrintedBook("Python Crash Course", "Eric Matthes", "22222", pages=544)

    # library.add_book(b1)
    # library.add_book(b2)
    # library.add_book(b3)
    # library.add_book(b4)

    # dup = PrintedBook("Duplicate Try", "Some Author", "12345", pages=100)
    # library.add_book(dup)  # duplicate ISBN -> warning

    # print("\nSearch title contains 'Python':")
    # for book in library.search_book("Python", by="title"):
    #     print("  -", book)

    # print("\nSearch author contains 'Brett':")
    # for book in library.search_book("Brett", by="author"):
    #     print("  -", book)

    # print("\nSearch by ISBN '22222':")
    # for book in library.search_book("22222", by="isbn"):
    #     print("  -", book)

    # print("\nRemoving ISBN '12345'...")
    # library.remove_book("12345")

    # print("\nFinal Library Books:")
    # for book in library.books:
    #     print("  -", book)