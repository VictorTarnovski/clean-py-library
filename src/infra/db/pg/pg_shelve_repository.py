from ....data.protocols.add_shelve_repository import AddShelveRepository
from ....domain.use_cases.add_shelve import Shelve, AddShelveParams
from ....domain.models.shelve import Shelve

class PGShelveRepository(AddShelveRepository):
    def add_shelve(self, add_shelve_params: AddShelveParams) -> Shelve:
      return {'id': 1, 'name': 'any_name'}