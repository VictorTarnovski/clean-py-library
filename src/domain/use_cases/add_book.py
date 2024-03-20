from ..models.book import Book


class AddBookParams:
    def __init__(self, name: str):
        self.name = name

class AddBook:
    def add(self, add_book_params: AddBookParams) -> Book | None:
        pass
