from ....data.protocols.add_shelve_repository import AddShelveRepository

from ....domain.use_cases.add_shelve import Shelve, AddShelveParams
from ....domain.models.shelve import Shelve

from .sql_query_builder import SQLQueryBuilder


class PGShelveRepository(AddShelveRepository):
    _table_name: str = "shelves"

    def add_shelve(self, add_shelve_params: AddShelveParams) -> Shelve:
        query = (
            SQLQueryBuilder()
            .insert_into(self._table_name)
            .fields(["name"])
            .values([add_shelve_params["name"]])
            .returning(["id", "name"])
        )

        shelve = query.execute()
        return shelve

    def find_by_id(self, shelve_id: str) -> Shelve:
        query = (
            SQLQueryBuilder()
            .select(["id", "name"])
            .from_table(self._table_name)
            .where(f"id = '{shelve_id}'")
            
        )
        shelve = query.execute()
        return shelve