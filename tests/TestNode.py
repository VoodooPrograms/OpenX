import unittest

from src.Node import Node, Tree


class TestNode(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(5)
        self.n1.left = Node(3)
        self.n1.right = Node(7)
        self.n1.left.left = Node(2)
        self.n1.left.right = Node(5)
        self.n1.right.left = Node(1)
        self.n1.right.right = Node(0)
        self.n1.right.right.left = Node(2)
        self.n1.right.right.right = Node(8)
        self.n1.right.right.right.right = Node(5)

    def test_sum(self):
        pass

    def test_avg(self):
        pass

    def test_mediana(self):
        pass
