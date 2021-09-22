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
