from openbiolink.nodeType import NodeType
from openbiolink.namespace import Namespace

class Node :
    def __init__(self, id: str, type : NodeType, namespace : Namespace, name = "" ):
        self.id = id
        self.type = type
        self.namespace = namespace

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash( (self.id, self.type))

    def __iter__(self):
        return iter([self.id, self.type])