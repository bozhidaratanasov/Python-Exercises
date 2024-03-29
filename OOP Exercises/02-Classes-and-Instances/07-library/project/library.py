class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user: 'User'):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user: 'User'):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        if user.username in self.rented_books:
            del self.rented_books[user.username]
        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        for user in self.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - it should be " \
                           "different than the username used so far!"
                if user.username in self.rented_books:
                    self.rented_books[new_username] = self.rented_books[user.username]
                    del self.rented_books[user.username]
                user.username = new_username
                return f"Username succesfully changed to: {new_username} for userid: {user_id}"
        return f"There is no user with id = {user_id}!"