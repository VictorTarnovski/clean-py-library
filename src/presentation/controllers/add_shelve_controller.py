from ..protocols.http_request import Request
from ..protocols.controller import Controller
from ..protocols.validation import Validation
from ..helpers.http import BadRequest, OK, ServerError
from ...domain.use_cases.add_shelve import AddShelve


class AddShelveRequest(Request):
    def __init__(self, name: str):
        super().__init__()
        self.name = name


class AddShelveController(Controller):
    def __init__(self, validation: Validation, add_shelve: AddShelve):
        self._validation = validation
        self._add_shelve = add_shelve

    def handle(self, request: AddShelveRequest):
        try:
            try:
                self._validation.validate(request)
            except Exception as exception:
                return BadRequest(exception)

            shelve = self._add_shelve.add(request)
            return OK(shelve)
        except:
            return ServerError()
