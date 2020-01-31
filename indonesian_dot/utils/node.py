class Node:
    def __init__(self, parent, values):
        # Node attribute
        self.parent = parent
        # numpy.ndarray attribute
        self.values = values

    # Mutators
    def set_parent(self, parent):
        self.parent = parent

    def set_values(self, values):
        self.values = values

    # Accessors
    def get_parent(self):
        return self.parent

    def get_values(self):
        return self.values
