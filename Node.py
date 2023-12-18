class Node:

    def __init__(self, name=None, prob=None):
        self.name = name

        self.prob = prob

        self.code = ""

        self.left = None

        self.right = None

    def __lt__(self, other):
        return self.prob < other.prob

    def __hash__(self):
        return hash((self.name, self.prob))

    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.name, self.prob) == (other.name, other.prob)

        return False

    def set_children(self, left, right):
        self.left = left
        self.right = right

    def build_code(self, code=""):
        self.code = code
        if self.left:
            self.left.build_code(code + "0")
        if self.right:
            self.right.build_code(code + "1")



