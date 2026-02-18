def teatro(usuario):
    while True:
        print("\n=== TEATRO AMAZONAS ===")
        print("1. Assistir a uma peça")
        print("2. Voltar para o menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\nAssistindo a uma peça...")
            # Lógica de assistir a uma peça aqui
        elif opcao == '2':
            print("Voltando para o menu principal...")
            break
        else:
            print("Opção inválida! Tente novamente.")