class FieldNotFoundException(Exception):
    def __init__(self, field_name: str):
        self.field_name = field_name
        super().__init__(f'{self.field_name}')
