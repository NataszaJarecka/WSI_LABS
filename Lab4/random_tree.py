from node_class import Node
from collections import Counter
import random
from data_operations import best_split



def build_random_tree(features: tuple, y: list, s: int, max_depth: int):
    root = Node((features, y))
    Q = [root]
    depth = 0

    while Q:
        node = Q.pop(0)
        node_features, node_y = node.data


        if all(label == node_y[0] for label in node_y) or depth >= max_depth:
            node.is_a_leaf()
            node.prediction = Counter(node_y).most_common(1)[0][0]
            continue


        feature_indices = list(range(len(features)))
        chosen_indices = random.sample(feature_indices, min(s, len(feature_indices)))

        best_feature = None
        best_subset = None
        best_ig = -1

        for i in chosen_indices:
            feature_column = features[i]
            subset, ig = best_split(feature_column, node_y)

            if ig > best_ig:
                best_ig = ig
                best_feature = i
                best_subset = subset

        if best_feature is None or best_subset is None:
            node.is_a_leaf()
            node.prediction = Counter(node_y).most_common(1)[0][0]
            continue


        node.best_feature = best_feature
        node.best_subset = best_subset


        left_features = [[] for _ in features]
        right_features = [[] for _ in features]
        left_y = []
        right_y = []

        for i in range(len(node_y)):
            if features[best_feature][i] in best_subset:
                for j in range(len(features)):
                    left_features[j].append(features[j][i])
                left_y.append(node_y[i])
            else:
                for j in range(len(features)):
                    right_features[j].append(features[j][i])
                right_y.append(node_y[i])


        left_node = Node((tuple(left_features), left_y))
        right_node = Node((tuple(right_features), right_y))
        node.left = left_node
        node.right = right_node


        Q.append(left_node)
        Q.append(right_node)

        depth += 1

    return root

def classify(node, element_features: tuple):

    while node.left is not None and node.right is not None:
        feature_value = element_features[node.best_feature]
        if feature_value in node.best_subset:
            node = node.left
        else:
            node = node.right

    return node.prediction





