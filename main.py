from libary import Library
from user import User

def main():
    library = Library()
    user = User(name="John Doe")

    # Adding some books to the library
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 3)
    library.add_book("1984", "George Orwell", 5)
    library.add_book("To Kill a Mockingbird", "Harper Lee", 2)

    while True:
        print("\n=== Library Management System ===")
        print("1. Display Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View Borrowed Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nBooks in the Library:")
            print(library.display_books())

        elif choice == "2":
            book_title = input("\nEnter the title of the book to borrow: ")
            book = library.find_book(book_title)
            if book:
                if user.borrow_book(book):
                    print(f"You have successfully borrowed '{book.title}'.")
                else:
                    print(f"'{book.title}' is not available.")
            else:
                print("Book not found.")

        elif choice == "3":
            book_title = input("\nEnter the title of the book to return: ")
            book = library.find_book(book_title)
            if book and user.return_book(book):
                print(f"You have successfully returned '{book.title}'.")
            else:
                print("You haven't borrowed this book or it doesn't exist.")

        


if __name__ == "__main__":
    main()
