import json
import os


ARQUIVO_DB = "/home/darkcover/Documentos/RPG/version1/BancoDados/Personagens.json"
ATRIBUTOS_BASE = "/home/darkcover/Documentos/RPG/version1/BancoDados/Jogo/atributosbase.json"

def criar_personagem(usuario):
    print(f"\n{usuario}, vamos criar um novo personagem.")

    nome = input("Digite o nome do personagem: ")

    # 🔹 Lista de classes disponíveis
    classes_disponiveis = ["Guerreiro da Aldeia", "Pajeh", "Caçador"]

    print("\nEscolha a classe:")
    for i, classe in enumerate(classes_disponiveis, start=1):
        print(f"{i} - {classe}")

    # 🔹 Validação com try/except
    while True:
        try:
            escolha = int(input("Digite o número da classe: "))

            if 1 <= escolha <= len(classes_disponiveis):
                classe_escolhida = classes_disponiveis[escolha - 1]
                break
            else:
                print("❌ Opção inválida. Escolha um número da lista.")

        except ValueError:
            print("❌ Entrada inválida. Digite apenas números.")

    novo_personagem = {
        "nome": nome,
        "classe": classe_escolhida,
        "nivel": 1
    }

    # 🔹 Se o arquivo não existir, cria um banco vazio
    if not os.path.exists(ARQUIVO_DB):
        with open(ARQUIVO_DB, "w") as f:
            json.dump({}, f)

    # 🔹 Carrega banco atual
    with open(ARQUIVO_DB, "r") as f:
        dados = json.load(f)

    # 🔹 Se usuário não existir, cria lista
    if usuario not in dados:
        dados[usuario] = []

    # 🔹 Adiciona personagem
    dados[usuario].append(novo_personagem)

    # 🔹 Salva novamente
    with open(ARQUIVO_DB, "w") as f:
        json.dump(dados, f, indent=4)

    print(f"\n✅ Personagem '{nome}' da classe '{classe_escolhida}' criado com sucesso!")
