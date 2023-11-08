class FieldNotFoundException(Exception):
  def __init__(self, fieldName: str):
    self.fieldName = fieldName
    super().__init__(f'{self.fieldName}')