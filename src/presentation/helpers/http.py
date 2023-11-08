from ..protocols.http_response import Response

class BadRequest(Response):
  def __init__(self, exception: Exception):
    self.exception = exception.__repr__()
    super().__init__(400, { 'exception': self.exception })

class OK(Response):
  def __init__(self, content):
    self.content = content
    super().__init__(200, self.content)