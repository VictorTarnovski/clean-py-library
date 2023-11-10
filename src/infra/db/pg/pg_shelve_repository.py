from ....data.protocols.add_shelve_repository import AddShelveRepository
from ....domain.use_cases.add_shelve import Shelve, AddShelveParams
from ....domain.models.shelve import Shelve
from .psycopg2_helper import SQLQueryBuilder


class PGShelveRepository(AddShelveRepository):
    def add_shelve(self, add_shelve_params: AddShelveParams) -> Shelve:
        query = (
            SQLQueryBuilder()
            .insert("shelves")
            .fields(["name"])
            .values([add_shelve_params["name"]])
            .returning(["id", "name"])
        )
        shelve = query.execute()
        return shelve
