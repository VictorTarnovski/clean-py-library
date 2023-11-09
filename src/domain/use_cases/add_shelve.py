from ..models.shelve import Shelve

class AddShelveParams:
  def __init__(self, name: str):
    self.name = name

class AddShelve:
    def __init__(self, shelve_repository):
        self._shelve_repository = shelve_repository

    def add(add_shelve_params: AddShelveParams) -> Shelve:
        shelve = self._shelve_repository.add_shelve(add_shelve_params)
        return shelve
