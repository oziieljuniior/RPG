from Jogo.Eventos.dia import eventodialooper


def iniciar_jogo(usuario, personagem):
    while True:
        print("\n==============================")
        print("🎮 AVENTURA - Cidade de Manaus")
        print(f"Jogador: {usuario}")
        print(f"Personagem: {personagem['nome']} ({personagem['classe']})")
        print(f'Nível: {personagem['nivel']} (xp {personagem['xp']} / {personagem['xp_complementar']})')
        print(f'Dia: {personagem['dia']}')
        print("==============================")
        
        print("\nEvento Dia")
        eventodialooper(personagem['nome'],personagem['nivel'],personagem['xp'],personagem['dia'])
        print("\n=== TELA DO JOGO ===")
        
        print("[1] Cuia Furada")
        print("[2] Adega")
        print("[3] Teatro Amazonas")
        print("[4] Personagem")
        print("[5] Campos de Treinamento")
        print("[6] Sortimentos Variados")
        print("[7] Ferreiro")
        print("[8] Caldeirão Borbulhante")
        print("[9] Diário")
        print("[10] Mapa")
        print("[11] Salvar e Sair")

        try:
            opcao = int(input("Entrada > "))
        except ValueError:
            print("Entrada inválida!")
            continue

        if opcao == 1:
            print("Você explora a região...")
            # Futuramente chamar módulo de exploração
        elif opcao == 2:
            print("\n=== STATUS ===")
            for chave, valor in personagem.items():
                print(f"{chave.capitalize()}: {valor}")
        elif opcao == 11:
            print("Salvando progresso...")
            break
        else:
            print("Opção inválida!")
