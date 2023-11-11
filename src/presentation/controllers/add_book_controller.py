from ..protocols.http_request import Request
from ..protocols.controller import Controller
from ..protocols.validation import Validation
from ..helpers.http import BadRequest, OK, ServerError
from ...domain.use_cases.add_book import AddBook


class AddBookRequest(Request):
    def __init__(self, name: str):
        super().__init__()
        self.name = name


class AddBookController(Controller):
    def __init__(self, validation: Validation, add_book: AddBook):
        self._validation = validation
        self._add_book = add_book

    def handle(self, request: AddBookRequest):
        try:
            try:
                self._validation.validate(request)
            except Exception as exception:
                return BadRequest(exception)

            book = self._add_book.add(request)
            return OK(book)
        except Exception as exception:
            print(exception)
            return ServerError(exception)
