class Node:

    def __init__(self):
        self._pv = None
        self._shield = None
        self._father = None
        self._child = []
        self._level = 0

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, value: int):
        self._pv = value

    @property
    def shield(self):
        return self._shield

    @shield.setter
    def shield(self, value: int):
        self._shield = value

    @property
    def father(self):
        return self._father

    @father.setter
    def father(self, value):
        self._father = value

    @property
    def child(self):
        return self._child

    @child.setter
    def child(self, value):
        self._child = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value: int):
        self._level = value

    def upgrade(self):
        self._level += 1


class LeaderNode(Node):

    def __init__(self, ):
        super().__init__()


class DefenseNode(Node):

    def __init__(self):
        super().__init__()


class HeadDefenseNode(DefenseNode):

    def __init__(self):
        super().__init__()


class AttackNode(Node):

    def __init__(self):
        super().__init__()


class HeadAttackNode(AttackNode):

    def __init__(self):
        super().__init__()


class ProductionNode(Node):

    def __init__(self):
        super().__init__()


class HeadProductionNode(ProductionNode):

    def __init__(self):
        super().__init__()
