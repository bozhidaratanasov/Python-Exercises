

class Equipment:
    _id = 1

    def __init__(self, name):
        self.name = name
        self.id = self._id
        self.__class__._id += 1

    @classmethod
    def get_next_id(cls):
        return cls._id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

