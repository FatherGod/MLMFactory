from abc import ABC, abstractmethod
import json
from enum import Enum

with open("initial_parameter.json", "r") as f:
    init_param = json.load(f)

class NodeType(Enum):
    ATTACK = 0
    DEFENSE = 1
    RESOURCE = 2
    MASTER = 3

class ProductType(Enum):
    COIN = 0
    MILITARY = 1
    PROTECTION = 2

class Node(ABC):
    def __init__(self, user):
        self.user = user
        self.pv = init_param["pv"]
        self.father = None
        self.child = []
        self.level = init_param["level"]
        self.xp = init_param["xp"]
        self.protector = None

    def getFather(self):
        return self.father

    def getPV(self):
        return self.pv

    def getChildren(self):
        return self.child

    def getUser(self):
        return self.user

    @abstractmethod
    def upgrade(self):
        self.level += 1

    def addChild(self, node):
        self.child.append(node)

    def removeChild(self, node):
        for child in self.child:
            if child == node:
                self.child.remove(child)
                return True
        return False

    def __str__(self):
        return f"User : {self.user} | PV : {self.pv} | Father : {self.father} | Level : {self.level}"
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.user == other.user
        return False
class AttackNode(Node):
    def __init__(self, user):
        self.power = init_param["attack"]
        self.target = None
        super().__init__(user)

    def attack(self):
        print("Node attack")

    def upgrade(self):
        super().upgrade()

    def __str__(self):
        return super().__str__() + f" | Attack : {self.power}"

class DefenseNode(Node):

    def __init__(self, user):
        self.defense = init_param["defense"]
        self.target = None
        super().__init__(user)

    def protect(self):
        print("Node protect")

    def upgrade(self):
        super().upgrade()

    def __str__(self):
        return super().__str__() + f" | Defense : {self.defense}"

class ResourceNode(Node):

    def __init__(self, user):
        self.resource_type = None
        self.prod_speed = init_param["production_speed"]
        super().__init__(user)

class MasterNode(Node):

    def __init__(self, user):
        self.spell = []
        super().__init__(user)

    def upgrade(self):
        super().upgrade()

    def __str__(self):
        return "Master -> " + super().__str__()

