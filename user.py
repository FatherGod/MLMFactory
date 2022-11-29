from node import NodeType

class User:

    def __init__(self, name, info):
        self.name = name
        self.info = info
        self.current_node = None
        self.attack_node = None
        self.defense_node = None
        self.resource_node = None
        self.type_node = None

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

    def switch_node(self, new_type):
        if self.type_node != NodeType.MASTER:
            if new_type != self.type_node:
                self.type_node = new_type
                if self.type_node == NodeType.ATTACK:
                    self.current_node = self.attack_node
                elif self.type_node == NodeType.DEFENSE:
                    self.current_node = self.defense_node
                else:
                    self.current_node = self.resource_node