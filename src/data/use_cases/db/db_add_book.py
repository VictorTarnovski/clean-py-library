from ....domain.use_cases.add_book import AddBook, AddBookParams
from ....domain.models.book import Book
from ....data.protocols.add_book_repository import AddBookRepository

class DbAddBook(AddBook):
    def __init__(self, add_book_repository: AddBookRepository):
        self._add_book_repository = add_book_repository
    
    def add(self, add_book_params: AddBookParams) -> Book:
        return self._add_book_repository.add_book(add_book_params)