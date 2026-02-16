from Jogo.Configuracoes.SelecionarPersonagem import selecionar_personagem
from Jogo.Configuracoes.CriarPersonagem import criar_personagem
from Jogo.game import iniciar_jogo

def menu_jogo(usuario):
    while True:
        print("\n=== MENU DO JOGO ===")
        print(f"Jogador: {usuario}")
        print("[1] Selecionar Personagem")
        print("[2] Novo Personagem")
        print("[0] Sair para Menu Principal")

        try:
            opcao = int(input("Entrada > "))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        if opcao == 1:
            personagem = selecionar_personagem(usuario)
            if personagem:
                print("Abrindo jogo ...")
                iniciar_jogo(usuario, personagem)
        elif opcao == 2:
            criar_personagem(usuario)
        elif opcao == 0:
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida!")

