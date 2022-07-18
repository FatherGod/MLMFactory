from node import AttackNode, DefenseNode, ProductionNode
from utils import NodeType, RulesError


class Player():

    def __init__(self):
        self._name = ""
        self._attack_node = AttackNode()
        self._defense_node = DefenseNode()
        self._production_node = ProductionNode()
        self._node_type = None
        self._salary = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value: NodeType):
        self._node_type = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def upgrade(self, node_type:NodeType, cost:int):
        if self.salary < cost:
            raise RulesError(f"Not enough money --> Stock : {self.salary} || Cost : {cost}")
        else:
            if node_type == NodeType.ATTACK:
                self._attack_node.upgrade()
                self._salary -= cost
            elif node_type == NodeType.DEFENSE:
                self._defense_node.upgrade()
                self._salary -= cost
            elif node_type == NodeType.PRODUCTION:
                self._production_node.upgrade()
                self._salary -= cost
            else:
                raise TypeError("Node Type not define")

    def get_salary(self, salary):
        self._salary += salary