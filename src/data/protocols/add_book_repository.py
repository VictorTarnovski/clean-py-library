from ...domain.use_cases.add_book import AddBookParams
from ...domain.models.book import Book


class AddBookRepository:
    def add_book(self, add_book_params: AddBookParams) -> Book:
        pass
