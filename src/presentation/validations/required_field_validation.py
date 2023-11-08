from ..protocols.validation import Validation
from ..protocols.http_request import Request
from ..exceptions.field_not_found_exception import FieldNotFoundException

class RequiredFieldValidation(Validation):
  def __init__(self, fieldName: str):
    self.fieldName = fieldName

  def validate(self, request: Request) -> None:
    if request.get(self.fieldName) == None:
      raise FieldNotFoundException(self.fieldName)
    else:
      return None