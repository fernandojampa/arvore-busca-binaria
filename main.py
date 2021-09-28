from binarySearchTree import BinarySearchTree
tree = BinarySearchTree()
texto = []


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
            if frase.replace(" ","").isalpha():
              texto = frase.split()
              tree = BinarySearchTree()
              print ("\nTexto inserido com sucesso!")
              for p in texto:
                tree.insert(p)
            else:
              print("\nTexto inserido inválido. Por favor, digite uma frase contendo apenas letras.")

        elif opcao == 'e':
            print('\nAscendente')
            tree.ascendente()
            print()
            print('\nDescendente')
            tree.descendente()
            print()

        elif opcao == 'c':
            tree.frequencia(texto)

        elif opcao == 'b':
          try:
            tree.balanceamento()
          except AttributeError:
            print ("\nErro na operação. Nenhum texto foi inserido. Por favor, digite um texto e tente novamente")

        elif opcao == 's':
            break

        else:
            print(
                '\nOpção inválida. Por favor, insira um valor referente à uma das opções que estejam no menu. ')

        # Tratamento de erro caso o usuário pressione as teclas que encerram a aplicação.

    except KeyboardInterrupt:
        print('\n !- Erro na Operação -!')
        print('\nComando de teclas pare encerrar a aplia escolhapressionadas. Por favor, para sair do programa, insira a opção correspondente, no menu principal.')
