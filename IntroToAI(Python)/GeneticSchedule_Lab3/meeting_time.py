class MeetingTime:
    def __init__(self, id: str, time: str):
        self.id = id
        self.time = time

    def __str__(self):
        return f"{self.time}"
