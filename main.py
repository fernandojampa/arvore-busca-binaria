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
            pass

        elif opcao == 'e':
            pass

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
