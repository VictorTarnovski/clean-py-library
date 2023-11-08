from ...presentation.controllers import AddShelveController
from ...presentation.validations.required_field_validation import (
    RequiredFieldValidation,
)
from ...presentation.protocols.validation import ValidationComposite


def makeAddShelveController() -> AddShelveController:
    validations = []
    validations.append(RequiredFieldValidation("name"))
    validation = ValidationComposite(validations)
    return AddShelveController(validation)
