def sortimentos(usuario):
    while True:
        print("\n=== SORTIMENTOS VARIADOS ===")
        print("1. Comprar Itens")
        print("2. Voltar para o menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\nComprando itens...")
            # Lógica de compra de itens aqui
        elif opcao == '2':
            print("Voltando para o menu principal...")
            break
        else:
            print("Opção inválida! Tente novamente.")