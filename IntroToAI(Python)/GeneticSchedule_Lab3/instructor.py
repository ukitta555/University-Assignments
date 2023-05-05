class Instructor:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name