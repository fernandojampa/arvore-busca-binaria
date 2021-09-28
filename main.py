from binarySearchTree import BinarySearchTree
from binaryTree import TreeException
tree = BinarySearchTree()
texto = []

# Menu do programa principal
while True:
    try:

        print('''
      Árvores Binárias de Busca

      (d) Digitar texto
      (e) Exibir palavras do texto Ascendente/Descendente
      (c) Exibir frequência de ocorrência das palavras
      (b) Mostrar o nível de desbalanceamento da árvore
      (s) Sair
            ''')

        opcao = input('Insira a opção desejada: ').lower()

        if opcao == 'd':

            frase = input('Digite a frase: ')
            if frase.replace(" ", "").isalpha():
                texto = frase.split()
                tree = BinarySearchTree()
                print("\nTexto inserido com sucesso!")
                for p in texto:
                    tree.insert(p)
            else:
                print(
                    "\nTexto inserido inválido. Por favor, digite uma frase contendo apenas letras.")

        # elif opcao == 'e':
           # if len(texto) == 0:
            #  print ("\nErro na operação. Nenhum texto foi inserido. Por favor, digite um texto e tente novamente")
            # else:
             # print('\nAscendente')
             # tree.ascendente()
             # print()
             # print('\nDescendente')
             # tree.descendente()
             # print()

        elif opcao == 'e':
            if tree.vazia() == False:
                try:
                    print('\nAscendente')
                    tree.ascendente()

                    print()
                    print('\nDescendente')
                    tree.descendente()
                    print()
                except TreeException as e:
                    print(e)
            else:
                print(
                    '\nErro na operação. Nenhum texto foi inserido. Por favor, digite um texto e tente novamente')

        elif opcao == 'c':

           # if len(texto) == 0:
           #   print ("\nErro na operação. Nenhum texto foi inserido. Por favor, digite um texto e tente novamente")
           # else:
            try:
                tree.frequencia(texto)
            except TreeException as e:
                print(e)

        elif opcao == 'b':
            try:
                tree.balanceamento()
            except TreeException as e:
                print(e)

        elif opcao == 's':
            break

        else:
            print(
                '\nOpção inválida. Por favor, insira um valor referente à uma das opções que estejam no menu. ')

        # Tratamento de erro caso o usuário pressione as teclas que encerram a aplicação.

    except KeyboardInterrupt:
        print('\n !- Erro na Operação -!')
        print('\nComando de teclas pare encerrar a aplia escolhapressionadas. Por favor, para sair do programa, insira a opção correspondente, no menu principal.')
