from ....domain.use_cases.add_shelve import AddShelve, AddShelveParams
from ....domain.models.shelve import Shelve
from ....data.protocols.add_shelve_repository import AddShelveRepository

class DbAddShelve(AddShelve):
    def __init__(self, add_shelve_repository: AddShelveRepository):
        self._add_shelve_repository = add_shelve_repository
    
    def add(self, add_shelve_params: AddShelveParams) -> Shelve:
        return self._add_shelve_repository.add_shelve(add_shelve_params)