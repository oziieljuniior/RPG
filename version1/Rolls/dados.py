import random

def d4():
    return random.randint(1,4)    

def d6():
    return random.randint(1,6)

def d8():
    return random.randint(1,8)

def d10():
    return random.randint(1,10)

def d12():
    return random.randint(1,12)

def d20(): # Dado para calcular o valor da vida base do personagem, o valor mínimo é 10 para evitar personagens com vida muito baixa.
    return random.randint(1,20)

def d24():
    return random.randint(1,24)

def d32():
    return random.randint(1,32)

def d64():
    return random.randint(1,64)

def d100():
    return random.randint(1,100)

def dranged10():
    transforma = random.randint(0,100) / 100
    return transforma


