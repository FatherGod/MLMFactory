class User:

    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.node = None

    def getName(self):
        return self.name

    def getInfo(self):
        return self.info

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.getName()
        return False

    def __str__(self):
        return f"Name : {self.name}"