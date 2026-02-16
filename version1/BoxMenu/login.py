import json
import os


def carregar_contas():
    caminho = os.path.join(
        os.path.dirname(__file__),
        "..",
        "BancoDados",
        "Contas.json"
    )

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def realizar_login():
    dados = carregar_contas()
    usuarios = dados.get("usuarios", [])

    print("\n=== LOGIN ===")

    username = input("Usuário: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario["username"] == username and usuario["senha"] == senha:
            print("\nLogin realizado com sucesso!")
            return username  # retorna o nome

    print("\nUsuário ou senha incorretos.")
    return None
