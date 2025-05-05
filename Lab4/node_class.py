class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.prediction = None
        self.best_feature = None
        self.best_subset = None
        self.leaf = False

    def is_a_leaf(self):
        self.leaf = True
