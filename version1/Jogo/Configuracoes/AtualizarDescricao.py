import json
import os

ARQUIVO_DB = "/home/darkcover/Documentos/RPG/version1/BancoDados/Personagens.json"

def atualizar_json(novos_dados):
    if not os.path.exists(ARQUIVO_DB):
        raise FileNotFoundError(f"Arquivo não encontrado: {ARQUIVO_DB}")
    
    # Lê os dados atuais
    with open(ARQUIVO_DB, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    
    #print("Dados atuais:", dados)
    #print("Novos dados:", novos_dados)

    nome_alvo = novos_dados.get("nome")
    atualizado = False

    for jogador, lista_personagens in dados.items():
        for i, personagem in enumerate(lista_personagens):
            #print("Comparando:", personagem.get("nome"), "com", nome_alvo)
            
            if personagem.get("nome") == nome_alvo:
                #dados[jogador][i].update(novos_dados)
                print("Personagem atualizado:", dados[jogador][i])
                atualizado = True
                break

    if atualizado:
        # 🔥 SALVA DE VOLTA NO ARQUIVO
        with open(ARQUIVO_DB, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        print("Arquivo salvo com sucesso!")
        return True
    
    print("Personagem não encontrado para atualização.")
    return False
