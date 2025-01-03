from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies):
        book = Book(title, author, copies)
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        if not self.books:
            return "No books available in the library."
        return "\n".join(str(book) for book in self.books)
