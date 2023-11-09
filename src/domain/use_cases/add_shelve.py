from ..models.shelve import Shelve


class AddShelveParams:
    name: str
    def __init__(self, name: str):
        pass


class AddShelve:
    def add(add_shelve_params: AddShelveParams) -> Shelve:
        pass
