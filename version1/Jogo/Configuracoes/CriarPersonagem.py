import json
import os
from Rolls.dados import d20


ARQUIVO_DB = "/home/darkcover/Documentos/RPG/version1/BancoDados/Personagens.json"
ATRIBUTOS_BASE = "/home/darkcover/Documentos/RPG/version1/BancoDados/Jogo/atributosbase.json"


def carregar_atributos_base():
    """Carrega os atributos base do arquivo JSON."""
    with open(ATRIBUTOS_BASE, "r", encoding="utf-8") as f:
        return json.load(f)


def criar_personagem(usuario):
    print(f"\n{usuario}, vamos criar um novo personagem.")

    nome = input("Digite o nome do personagem: ")

    # 🔹 Lista de classes disponíveis
    classes_disponiveis = ["Guerreiro", "Paje", "Cacador"]

    print("\nEscolha a classe:")
    for i, classe in enumerate(classes_disponiveis, start=1):
        print(f"{i} - {classe}")

    # 🔹 Validação da escolha
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

    # 🔹 Vida inicial baseada em d20 (mínimo 10)
    while True:
        eventovida = d20()
        if eventovida >= 10:
            break

    # 🔹 Carrega atributos base corretamente
    atributos_base = carregar_atributos_base()

    # 🔹 Garante que a classe exista no JSON
    if classe_escolhida not in atributos_base:
        print("❌ Classe não encontrada nos atributos base.")
        return

    atributos_classe = atributos_base[classe_escolhida]

    # 🔹 Criação do personagem
    novo_personagem = {
        "nome": nome,
        "classe": classe_escolhida,
        "nivel": 1,
        "xp": 0,
        "xp_complementar": 10,
        "dia": 1,
        "vida": eventovida,
        "bravura": atributos_classe["Bravura"],
        "destreza": atributos_classe["Destreza"],
        "conexao_espiritual": atributos_classe["Conexao_Espiritual"],
        "resistencia": atributos_classe["Resistencia"],
        "harmonia": atributos_classe["Harmonia"]
    }

    # 🔹 Se o arquivo não existir, cria banco vazio
    if not os.path.exists(ARQUIVO_DB):
        with open(ARQUIVO_DB, "w", encoding="utf-8") as f:
            json.dump({}, f)

    # 🔹 Carrega banco atual
    with open(ARQUIVO_DB, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # 🔹 Se usuário não existir, cria lista
    if usuario not in dados:
        dados[usuario] = []

    # 🔹 Adiciona personagem
    dados[usuario].append(novo_personagem)

    # 🔹 Salva novamente
    with open(ARQUIVO_DB, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"\n✅ Personagem '{nome}' da classe '{classe_escolhida}' criado com sucesso!")
