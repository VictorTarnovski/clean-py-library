from ...presentation.protocols.controller import Controller
from ...presentation.controllers import InternalServerErrorProxy

def makeInternalServerErrorProxy(controller: Controller) -> InternalServerErrorProxy:
    return InternalServerErrorProxy(controller)
