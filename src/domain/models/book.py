class Book:
    id: str

    def __init__(self, name: str, authors: list[str]):
        self.name = name
        self.authors = authors
        self.shelves = []
