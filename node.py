from binaryTreeException import BinaryTreeException


class Node:
    def __init__(self, dado=None):
        self.__dado = dado
        self.__esq = None
        self.__dir = None
        self.__pai = None

    # get
    @property
    def dado(self):
        return self.__dado

    # set
    @dado.setter
    def dado(self, novo):
        self.__dado = novo

    # get
    @property
    def esq(self):
        return self.__esq

    # set
    @esq.setter
    def esq(self, novo):
        if self.__esq != None:
            raise BinaryTreeException('O nó esquerdo já existe')
        else:
            self.__esq = novo

    # get
    @property
    def dir(self):
        return self.__dir

    # set
    @dir.setter
    def dir(self, novo):
        if self.dir != None:
            raise BinaryTreeException('O nó direito já existe')
        else:
            self.__dir = novo

    # get
    @property
    def pai(self):
        return self.__pai

    # set
    @pai.setter
    def pai(self, novo):
        self.__pai = novo
