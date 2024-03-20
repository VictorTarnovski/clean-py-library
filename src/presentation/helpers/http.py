from ..protocols.http_response import Response
from ..exceptions import InternalServerErrorExeception

class OK(Response):
    def __init__(self, content):
        self._content = content
        super().__init__(200, self._content)

class BadRequest(Response):
    def __init__(self, exception: Exception):
        super().__init__(400, {'exception': exception.__repr__()})

class ServerError(Response):
    def __init__(self, exception: Exception):
        self._exception = exception.__repr__()
        super().__init__(500, { 'exception': InternalServerErrorExeception().__repr__()})