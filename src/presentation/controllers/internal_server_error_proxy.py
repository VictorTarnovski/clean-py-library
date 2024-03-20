from ..protocols.http_request import Request
from ..protocols.controller import Controller
from ..helpers.http import ServerError

class InternalServerErrorProxy(Controller):
    def __init__(self, controller: Controller):
        self._controller = controller

    def handle(self, request: Request):
        try:
            return self._controller.handle(request)
        except Exception as exception:
            print(exception)
            return ServerError(exception)
