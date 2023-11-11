from ....data.protocols.add_book_repository import AddBookRepository

from ....domain.use_cases.add_book import AddBookParams
from ....domain.models.book import Book

from .sql_query_builder import SQLQueryBuilder


class PGBookRepository(AddBookRepository):
    _table_name: str = "books"

    def add_book(self, add_book_params: AddBookParams) -> Book:
        query = (
            SQLQueryBuilder()
            .insert_into(self._table_name)
            .fields(["name"])
            .values([add_book_params["name"]])
            .returning(["id", "name"])
        )
        book = query.execute()
        return book

    def find_by_id(self, book_id: str) -> Book:
        query = (
            SQLQueryBuilder()
            .select(["id", "name", "authors"])
            .from_table(self._table_name)
            .where(f"id = '{book_id}'")
            
        )
        book = query.execute()
        return book