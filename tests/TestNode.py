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
        self.assertEqual(Tree.sum(self.n1), 38)

    def test_avg(self):
        self.assertEqual(Tree.avg(self.n1), 3.8)

    def test_mediana(self):
        self.assertEqual(Tree.mediana(self.n1), 4)
