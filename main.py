from library import Library

lib = Library()
lib.add_book("The Alchemist", "Paulo Coelho")
lib.add_book("1984", "George Orwell")
lib.add_user("Alice")
lib.add_user("Bob")

def menu():
    while True:
        print("\n=== Library Menu ===")
        print("1. View all books")
        print("2. View available books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.list_books(only_available=True)
        elif choice == "3":
            lib.list_books(only_available=True)
            book_idx = int(input("Enter book number: ")) - 1
            user_idx = int(input("Enter user (0: Alice, 1: Bob): "))
            lib.borrow_book(user_idx, book_idx)
        elif choice == "4":
            lib.list_books()
            book_idx = int(input("Enter book number to return: ")) - 1
            user_idx = int(input("Enter user (0: Alice, 1: Bob): "))
            lib.return_book(user_idx, book_idx)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

menu()
