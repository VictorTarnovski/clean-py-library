from ...presentation.controllers import AddBookController
from ...presentation.validations.required_field_validation import (
    RequiredFieldValidation,
)
from ...presentation.protocols.validation import ValidationComposite
from ...data.use_cases.db.db_add_book import DbAddBook
from ...infra.db.pg.pg_book_repository import PGBookRepository


def makeAddBookController() -> AddBookController:
    validations = []
    validations.append(RequiredFieldValidation("name"))
    validation = ValidationComposite(validations)

    book_repository = PGBookRepository()
    add_book = DbAddBook(book_repository)
    return AddBookController(validation, add_book)
