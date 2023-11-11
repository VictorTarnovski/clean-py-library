from ..protocols.http_response import Response


class BadRequest(Response):
    def __init__(self, exception: Exception):
        self._exception = exception.__repr__()
        super().__init__(400, {'exception': self._exception})


class OK(Response):
    def __init__(self, content):
        self._content = content
        super().__init__(200, self._content)

class ServerError(Response):
    def __init__(self, exception: Exception):
        self._exception = exception.__repr__()
        super().__init__(500, { 'exception': Exception("Internal Server Error").__repr__()})
