import json

with open("/home/darkcover/Documentos/RPG/version1/BancoDados/Jogo/dias.json", "r", encoding="utf-8") as arquivo:
    lore = json.load(arquivo)

DIAS_EVENTOS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

def eventodialooper(personagem, nivel, xp, dia):
    for n in range(len(DIAS_EVENTOS)):
        if dia == 1 and nivel == 1 and xp == 0 and DIAS_EVENTOS[n] == 1:
            print(lore['0']['Titulo'])
            print(lore['0']['descrição'])
            print("Evento: ", lore['0']['impacto'])
            break
    
    
    
