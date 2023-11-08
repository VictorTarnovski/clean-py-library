from .http_request import Request

class Validation:
  def validate(self, request: Request) -> None:
    pass

class ValidationComposite(Validation):
  def __init__(self, validations):
    self.validations = validations
  
  def validate(self, request: Request) -> None:
    for i in range(len(self.validations)):
      self.validations[i].validate(request)
    return None