class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: 'Library'):
        for key, value in library.rented_books.items():
            if book_name in value:
                return f"The books {book_name} is already rented and will be available in {library.rented_books[key][book_name]} days!"

        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            library.rented_books[self.username] = {book_name: days_to_return}
            return f"{book_name} succesfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library: 'Library'):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        library.books_available[author].append(book_name)
        del library.rented_books[self.username][book_name]
        self.books.remove(book_name)

    def info(self):
        return ", ".join(sorted(self.books))

    def __repr__(self):
        return f"{self.user_id}, {self.username}, {self.books}"