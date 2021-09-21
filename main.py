from node import Node
from binaryTree import BinaryTree
arvore = BinaryTree()

while True:
    try:

        print('''
      Árvores Binárias de Busca

      (d) Digitar texto
      (e) Exibir palavras do texto Ascendente/Descendente
      (c) Exibir frequência de ocorrência das palavras
      (s) Sair
            ''')

        opcao = input('Insira a opção desejada: ').lower()

        # Cadeia de ifs de acordo com as opções do menu

        # Opção para inserir o nome dos candidatos.

        if opcao == 'd':
            texto = input('Digite a frase: ')
            arvore.split(texto)

        elif opcao == 'e':
            print(arvore.exibirPalavras())

        # Opção para realizar o sorteio.

        elif opcao == 'c':
            pass

        elif opcao == 's':
            break

        # Estrutura de decisão para caso o usuário digite algum valor não referente a nenhuma opção no menu, fazendo com que o laço reinicie.

        else:
            print(
                '\nOpção inválida. Por favor, insira um valor referente à uma das opções que estejam no menu. ')

        # Tratamento de erro caso o usuário pressione as teclas que encerram a aplicação.

    except KeyboardInterrupt:
        print('\n !- Erro na Operação -!')
        print('\nComando de teclas pare encerrar a aplia escolhapressionadas. Por favor, para sair do programa, insira a opção correspondente, no menu principal.')


'''raiz = Node('A')
raiz.esq = Node('B')
raiz.dir = Node('C')

p = raiz.esq  # Nó B
q = raiz.dir  # Nó C

p.esq = Node('D')
p.dir = None

q.esq = Node('E')
q.dir = Node('F')

r = p.esq  # Nó D

r.esq = None
r.dir = Node('G')

r = q.esq

r.esq = Node('H')
r.dir = Node('I')

tree = BinaryTree()
tree.em_ordem(raiz)'''
