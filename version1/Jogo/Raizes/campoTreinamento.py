def campo(usuario):
    while True:
        print("\n=== CAMPOS DE TREINAMENTO ===")
        print("1. Treinar Habilidades")
        print("2. Voltar para o menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\nTreinando habilidades...")
            # Lógica de treinamento de habilidades aqui
        elif opcao == '2':
            print("Voltando para o menu principal...")
            break
        else:
            print("Opção inválida! Tente novamente.")