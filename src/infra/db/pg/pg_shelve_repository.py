import psycopg2

from ....data.protocols.add_shelve_repository import AddShelveRepository
from ....domain.use_cases.add_shelve import Shelve, AddShelveParams
from ....domain.models.shelve import Shelve


class PGShelveRepository(AddShelveRepository):
    def add_shelve(self, add_shelve_params: AddShelveParams) -> Shelve:
        conn = psycopg2.connect(
            host="localhost",
            dbname="secret_db",
            user="secret_user",
            password="secret_password",
            port=5432,
        )
        cur = conn.cursor()
        cur.execute(
            f"insert into shelves (name) values ('{add_shelve_params['name']}') returning id;"
        )
        conn.commit()
        shelve = self.findById(cur.fetchone()[0])
        return shelve

    def findById(self, id: str) -> Shelve:
        conn = psycopg2.connect(
            host="localhost",
            dbname="secret_db",
            user="secret_user",
            password="secret_password",
            port=5432,
        )
        cur = conn.cursor()
        cur.execute(f"select id, name from shelves where id = '{id}'")
        result_tuple = cur.fetchone()
        return {"id": result_tuple[0], "name": result_tuple[1]}
