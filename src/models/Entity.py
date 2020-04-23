import uuid


class Entity:
    def __init__(self):
        self.uuid = str(uuid.uuid4())[:2]
