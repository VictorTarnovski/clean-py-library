from ..protocols.http_request import Request
from ..protocols.http_response import Response
from ..protocols.controller import Controller
from ..protocols.validation import Validation
from ..helpers.http import BadRequest, OK

class AddShelveRequest(Request):
  def __init__(self, name: str):
    super().__init__()
    self.name = name

class AddShelveController(Controller):
  def __init__(self, validation: Validation):
    self.validation = validation

  def handle(self, request: AddShelveRequest):
    try:
      self.validation.validate(request)
    except Exception as exception:
      return BadRequest(exception)
    return OK(request)