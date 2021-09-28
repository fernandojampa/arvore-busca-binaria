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

    def balanceamento(self, node=None):

        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.altura(node.left)
        if node.right:
            hright = self.altura(node.right)

        # print(
        #     f'\nProfundidade da árvore esquerda: {hleft+1}\nProfundidade da árvore direita: {hright+1}')
        
        
        print(f'\nFator de balanceamento da árvore: {hleft - hright}')
        if hleft - hright == 1 or hleft - hright == 0 or hleft - hright == -1:
            print('Árvore balanceada')
        else:
            print('Árvore Desbalanceada')

    def altura(self, node=None):

        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.altura(node.left)
        if node.right:
            hright = self.altura(node.right)

        if hright > hleft:
            return hright + 1
        else:
            return hleft + 1
