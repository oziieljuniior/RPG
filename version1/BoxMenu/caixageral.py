from Jogo.menu import menu_jogo


def iniciar_menu(usuario):
    """
    Docstring para iniciar_menu
    
    :param usuario: usario passado no login
    """
    while True:
        print(12*'*', "Menu", 12*'*')
        print("[1] Jogo")
        print("[2] Configurações")
        print("[0] Sair")

        try:
            opcao = int(input("Entrada > "))
        except ValueError:
            print("Entrada inválida!")
            continue

        if opcao == 1:
            menu_jogo(usuario)
        elif opcao == 2:
            print("Configurações...")
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
