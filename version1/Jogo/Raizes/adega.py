def adega(usuario):
    while True:
        print("\n=== ADEGA ===")
        print("1. Treinar Combate")
        print("2. Voltar para o menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\nTreinando combate...")
            # Lógica de treinamento de combate aqui
        elif opcao == '2':
            print("Voltando para o menu principal...")
            break
        else:
            print("Opção inválida! Tente novamente.")
    