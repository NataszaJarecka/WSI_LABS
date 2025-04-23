class Node:
    def __init__(self, data):
        self.data = data  # Tuple: (features, y)
        self.left = None
        self.right = None
        self.prediction = None  # Tylko jeśli to liść
        self.best_feature = None  # Indeks najlepszej cechy (np. 2)
        self.best_subset = None   # Zbiór wartości cechy prowadzący do lewej gałęzi
        self.leaf = False         # Czy to liść

    def is_a_leaf(self):
        self.leaf = True
