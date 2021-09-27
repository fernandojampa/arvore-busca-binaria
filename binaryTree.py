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
    def ascendente(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.ascendente(node.left)
        print(node, end=' ')
        if node.right:
            self.ascendente(node.right)

    def descendente(self, node=None):
        if node is None:
            node = self.root
        if node.right:
            self.descendente(node.right)
        print(node, end=' ')
        if node.left:
            self.descendente(node.left)

    def frequencia(self, list):
        list = list
        counts = Counter(list)
        for i in counts:
            print(f'{i} = {counts[i]}')

    def altura(self, root):
        root = self.root
        if root is None:
            return 0
        return max(self.altura(root.left), self.altura(root.right)) + 1

    def balanceada(self):
        root = self.root
        altura_esq = self.altura(root.left)
        altura_dir = self.altura(root.right)
        # Alturas diferem em mais de uma unidade.
        if abs(altura_esq - altura_dir) > 1:
            return False

        return self.balanceada(root.left) and self.balanceada(root.right)

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
        else:
            return hleft + 1

    '''def balanceada(self, node=None):

        if node is None:
            node = self.root

        altura_esq = self.altura()
        altura_dir = self.altura()
        # Alturas diferem em mais de uma unidade.
        if abs(altura_esq - altura_dir) > 1:
            return False

        return self.balanceada(node.left) and self.balanceada(node.right)'''
