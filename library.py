from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_user(self, name):
        self.users.append(User(name))

    def list_books(self, only_available=False):
        for i, book in enumerate(self.books):
            if not only_available or not book.is_borrowed:
                print(f"{i + 1}. {book}")

    def borrow_book(self, user_index, book_index):
        user = self.users[user_index]
        book = self.books[book_index]
        if user.borrow_book(book):
            print(f"{user.name} borrowed '{book.title}'")
        else:
            print("Book already borrowed.")

    def return_book(self, user_index, book_index):
        user = self.users[user_index]
        book = self.books[book_index]
        if user.return_book(book):
            print(f"{user.name} returned '{book.title}'")
        else:
            print("This user didn't borrow that book.")
