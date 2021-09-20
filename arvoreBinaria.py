class BinaryTree:
    def __init__(self):
        self._frase = []

    def em_ordem(self, arvore):
        if arvore != None:
            self.em_ordem(arvore.esq)
            print(arvore.dado, end='')  # Visita a raiz
            self.em_ordem(arvore.dir)

    def split(self, frase):
        self._frase = frase.split()
        for i in range(len(self._frase)):
            print(self._frase[i])
