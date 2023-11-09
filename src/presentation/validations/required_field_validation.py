from ..protocols.validation import Validation
from ..protocols.http_request import Request
from ..exceptions.field_not_found_exception import FieldNotFoundException


class RequiredFieldValidation(Validation):
    def __init__(self, field_name: str):
        self.field_name = field_name

    def validate(self, request: Request) -> None:
        if request.get(self.field_name) is None:
            raise FieldNotFoundException(self.field_name)
        else:
            return None
