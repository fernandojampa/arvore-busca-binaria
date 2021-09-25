from collections import Counter
from node import Node
ROOT = "root"


class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Percurso em EM ORDEM em ÁRVORE BINÁRIA:
    def em_ordem(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.em_ordem(node.left)
        print(node, end=' ')
        if node.right:
            self.em_ordem(node.right)

    # Percurso em PÓS ORDEM em ÁRVORE BINÁRIA:
    def pos_ordem(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.pos_ordem(node.left)
        if node.right:
            self.pos_ordem(node.right)
        print(node, end=' ')

    def frequencia(self, list):
        list = list
        counts = Counter(list)
        for i in counts:
            print(f'{i} = {counts[i]}')

    def balanceamento(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.balanceamento(node.left)
        if node.right:
            hright = self.balanceamento(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
