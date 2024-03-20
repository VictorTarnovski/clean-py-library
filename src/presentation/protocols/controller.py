from .http_request import Request
from .http_response import Response


class Controller:
    def handle(self, request: Request) -> Response | None:
        pass
