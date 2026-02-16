from BoxMenu.caixageral import iniciar_menu
from BoxMenu.login import realizar_login


def main():
    print("Iniciando RPG")
    usuario = realizar_login()
    if usuario:
        print("Entrando no jogo...")
        iniciar_menu(usuario)
    else:
        print("Falha no login.")
    
    

if __name__ == "__main__":
    main()


