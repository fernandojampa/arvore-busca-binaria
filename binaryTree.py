from node import Node


class BinaryTree:
    def __init__(self):
        self._frase = []
        #self._abb = []

    def em_ordem(self, arvore):
        if arvore != None:
            self.em_ordem(arvore.esq)
            print(arvore.dado, end='')  # Visita a raiz
            self.em_ordem(arvore.dir)

    def split(self, frase):
        self._frase = frase.split()
        for i in range(len(self._frase)):
            if i == 0:
                raiz = Node(self._frase[i])
            elif self._frase[i] < raiz.dado:
                raiz.esq = Node(self._frase[i])
            elif self._frase[i] > raiz.dado:
                raiz.esq = Node(self._frase[i])

    def exibirPalavras(self):
        raiz = Node(self._frase[0])
        tree = BinaryTree()
        tree.em_ordem(raiz)
