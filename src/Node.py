

class Node:

    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:

    @staticmethod
    def sum(node) -> int:
        if node is None:
            return 0
        return Tree.sum(node.left) + Tree.sum(node.right) + node.value

    @staticmethod
    def avg(node):
        def helper(node, sum, count) -> tuple:
            if node is None:
                return (0, 0)
            else:
                (left_sum, left_count) = helper(node.left, 0, 0)
                (right_sum, right_count) = helper(node.right, 0, 0)
                return (node.value + left_sum + right_sum, 1 + left_count + right_count)
        (sum, count) = helper(node, 0, 0)
        return sum/count

    @staticmethod
    def mediana(node) -> float:
        sort_tree = lambda node: \
            [] if node is None else sorted(sort_tree(node.left) + [node.value] + sort_tree(node.right))
        sorted_tree = sort_tree(node)
        sorted_tree_len = len(sorted_tree)
        if sorted_tree_len % 2:
            return sorted_tree[sorted_tree_len // 2]
        else:
            return (sorted_tree[sorted_tree_len // 2 - 1] + sorted_tree[sorted_tree_len // 2]) / 2.0
