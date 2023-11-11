from ..models.book import Book


class AddBookParams:
    def __init__(self, name: str):
        self.name = name
        pass


class AddBook:
    def add(add_Book_params: AddBookParams) -> Book:
        pass
