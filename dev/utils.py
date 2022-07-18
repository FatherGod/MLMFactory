from enum import Enum

class NodeType(Enum):
    ATTACK = 0
    DEFENSE = 1
    PRODUCTION = 2

class RulesError(Exception):
    pass