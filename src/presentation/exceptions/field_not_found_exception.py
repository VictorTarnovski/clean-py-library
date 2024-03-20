class FieldNotFoundException(Exception):
    def __init__(self, field_name: str):
        super().__init__(f'{field_name}')
