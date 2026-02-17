def mapa(usuario):
    while True:
        print("Mapa da Região")
        print("┌─────────────────────────────┐")
        print("│  [0] Sair                   │")
        print("│  [1] Aldeia Ribeirinha      │")
        print("│  [2] Mata Fechada           │")
        print("│  [3] Rio Encatado           │")
        print("│  [4] Floresta Profunda      │")
        print("│  [5] Terras Corrompidas     │")
        print("└─────────────────────────────┘")
        
        try:
            opcao = int(input("Entrada > "))
        except ValueError:
            print("Entrada inválida!")
            continue
        
        if opcao == 0:
            print("Você decide sair do mapa.")
            break
        elif opcao == 1:
            print("Você se dirige à Aldeia Ribeirinha, um local pacífico às margens do rio.")
            # Futuramente chamar módulo de exploração da aldeia
        elif opcao == 2:
            print("Você adentra a Mata Fechada, onde a luz do sol mal penetra.")
            # Futuramente chamar módulo de exploração da mata
        elif opcao == 3:
            print("Você segue o Rio Encatado, cujas águas são ditas ter propriedades mágicas.")
            # Futuramente chamar módulo de exploração do rio
        elif opcao == 4:
            print("Você se aventura na Floresta Profunda, lar de criaturas misteriosas.")
            # Futuramente chamar módulo de exploração da floresta
        elif opcao == 5:
            print("Você se aproxima das Terras Corrompidas, onde a natureza parece estar morrendo.")
            # Futuramente chamar módulo de exploração das terras corrompidas
        else:
            print("Opção inválida! Por favor, escolha um local válido.")