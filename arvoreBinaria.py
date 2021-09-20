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
            no = Node()
            if i == 0:
                no.__pai = self._frase[i]
            elif i > 0:
                if self._frase[i] < no.__pai:
                    no.__esq = self._frase[i]
                elif self._frase[i] > no.__pai:
                    no.__dir = self._frase[i]
