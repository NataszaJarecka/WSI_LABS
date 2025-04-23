from collections import Counter
import math
import itertools

def entropy(y):
    total = len(y)
    counts = Counter(y)

    entropy = 0

    for count in counts.values():
        entropy -= (count/total) * math.log2(count/total)

    return entropy


def best_split(features, y):

    values = set(features)
    entropy_before = entropy(y)
    total = len(y)

    subsets = []
    for i in range(1, len(values)):
        subsets.extend(itertools.combinations(values, i))

    best_subset = None
    best_ig = -1

    for subset in subsets:
        left_y = [label for f, label in zip(features, y) if f in subset]
        right_y = [label for f, label in zip(features, y) if f not in subset]

        if not left_y or not right_y:
            continue

        weighted_entropy = (len(left_y) / total) * entropy(left_y) + \
                           (len(right_y) / total) * entropy(right_y)
        ig = entropy_before - weighted_entropy

        if ig > best_ig:
            best_ig = ig
            best_subset = subset

    return best_subset, best_ig