from ...presentation.controllers import AddShelveController
from ...presentation.validations.required_field_validation import (
    RequiredFieldValidation,
)
from ...presentation.protocols.validation import ValidationComposite
from ...data.use_cases.db.db_add_shelve import DbAddShelve
from ...infra.db.pg.pg_shelve_repository import PGShelveRepository


def makeAddShelveController() -> AddShelveController:
    validations = []
    validations.append(RequiredFieldValidation("name"))
    validation = ValidationComposite(validations)

    shelve_repository = PGShelveRepository()
    add_shelve = DbAddShelve(shelve_repository)
    return AddShelveController(validation, add_shelve)
