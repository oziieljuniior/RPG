from pathlib import Path
import json


def selecionar_personagem(usuario):
    print(f"\n{usuario}, selecione um personagem:")

    # Caminho base do projeto (version1)
    BASE_DIR = Path(__file__).resolve().parents[2]
    
    caminho = BASE_DIR / "BancoDados" / "Personagens.json"
    
    if not caminho.exists():
        print("Arquivo de personagens não encontrado.")
        print(f"Caminho procurado: {caminho}")
        return None

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    personagens = dados.get(usuario, [])

    if not personagens:
        print("Você ainda não possui personagens criados.")
        return None

    for i, personagem in enumerate(personagens, start=1):
        print(f"[{i}] {personagem['nome']} | Classe: {personagem['classe']} | Nível: {personagem['nivel']}")

    print("[0] Voltar")

    try:
        escolha = int(input("Entrada > "))
    except ValueError:
        print("Entrada inválida.")
        return None

    if escolha == 0:
        return None

    if 1 <= escolha <= len(personagens):
        selecionado = personagens[escolha - 1]
        print(f"\nPersonagem '{selecionado['nome']}' selecionado com sucesso!")
        return selecionado

    print("Opção inválida.")
    return None
