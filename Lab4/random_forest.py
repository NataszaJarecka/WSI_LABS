from random_tree import build_random_tree, classify
import numpy as np
from collections import Counter
import random

def bootstrap_sample(x, y):

    n = len(next(iter(x)))

    indices = random.choices(range(n), k=n)

    x_sample = tuple([col[i] for i in indices] for col in x)

    y_sample = [y[i] for i in indices]

    return x_sample, y_sample


def random_forest(features: tuple, y: list, s: int, max_depth: int, tree_amount: int, element_features:tuple):

    predictions = np.zeros(tree_amount)

    for i in range (tree_amount):

        X, Y = bootstrap_sample(features,y)
        tree = build_random_tree(X, Y, s, max_depth)
        prediction = classify(tree, element_features)
        predictions[i] = prediction

    c = Counter(predictions)
    result = c.most_common(1)
    classification = result[0][0]

    probability = c[1] / sum(c.values())
    return classification, probability

