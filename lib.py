library={}

def add_book(book_name):
    if book_name in library:
        print(f"'{book_name}' is already in the library.")
    else:
        library[book_name] = True  # True indicates the book is available.
        print(f"'{book_name}' has been added to the library.")

def view_books():
    if not library:
        print("The library is empty.")
    else:
        print("Books in the library:")
        for book, available in library.items():
            status = "Available" if available else "Borrowed"
            print(f" - {book}: {status}")

def borrow_book(book_name):
    if book_name in library:
        if library[book_name]:  # Check if the book is available.
            library[book_name] = False  # Mark the book as borrowed.
            print(f"You have borrowed '{book_name}'.")
        else:
            print(f"Sorry, '{book_name}' is currently borrowed.")
    else:
        print(f"'{book_name}' is not in the library.")

def return_book(book_name):
    if book_name in library:
        if not library[book_name]:  # Check if the book is borrowed.
            library[book_name] = True  # Mark the book as available.
            print(f"'{book_name}' has been returned. Thank you!")
        else:
            print(f"'{book_name}' was not borrowed.")
    else:
        print(f"'{book_name}' is not in the library.")


def main():
    print("Welcome to the Mini Library Management System!")

    while True:
        print("\nChoose an option:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_name = input("Enter the name of the book to add: ").strip()
            add_book(book_name)
        elif choice == "2":
            view_books()
        elif choice == "3":
            book_name = input("Enter the name of the book to borrow: ").strip()
            borrow_book(book_name)
        elif choice == "4":
            book_name = input("Enter the name of the book to return: ").strip()
            return_book(book_name)
        elif choice == "5":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
