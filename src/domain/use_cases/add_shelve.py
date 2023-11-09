from ..models.shelve import Shelve


class AddShelveParams:
    def __init__(self, name: str):
        self.name = name


class AddShelve:
    def add(add_shelve_params: AddShelveParams) -> Shelve:
        pass
