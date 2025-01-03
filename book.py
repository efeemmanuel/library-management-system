class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def is_available(self):
        return self.copies > 0

    def borrow(self):
        if self.is_available():
            self.copies -= 1
            return True
        return False

    def return_book(self):
        self.copies += 1

    def __str__(self):
        return f"{self.title} by {self.author} ({self.copies} copies available)"
