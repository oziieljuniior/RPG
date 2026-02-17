import os
from Rolls.dados import dranged10

def cuiafurada(personagem, controle1):
    while True:
        print("Menu Cuia Furada")
        print("[0] Sair do Cuia Furada")
        print("[1] Conversar com a tarveneira")
        print("[2] Subir para o quarto")
        
        try:
            opcao = int(input("Entrada > "))
        except ValueError:
            print("Entrada inválida!")
            continue  
        
        if opcao == 0:
            os.system("clear")
            print("Saindo do Cuia Furada...")
            break
        elif opcao == 1:
            valorSuprimento = suprimento_complementar(personagem)
            valorSanidade = sanidade_complementar(personagem)
            if controle1 == 1:
                chanceSuprimento = dranged10()*(personagem['harmonia']/100)*(personagem['sorte'])
                chanceSanidade = dranged10()*(personagem['harmonia']/100)*(personagem['sorte'])
                if chanceSuprimento >= 0.65:
                    if chanceSuprimento >= 0.90:
                        valorSuprimento = int(valorSuprimento * 0.5)  # 50% de desconto
                    else:
                        valorSuprimento = int(valorSuprimento * 0.8)  # 20% de desconto
                if chanceSanidade >= 0.65:
                    if chanceSanidade >= 0.90:
                        valorSanidade = int(valorSanidade * 0.5)  # 50% de desconto
                    else:
                        valorSanidade = int(valorSanidade * 0.8)  # 20% de desconto
                controle1 = 2
                
            while True:
                print("\nVocê conversa com o tarveneiro e descobre informações valiosas.")
                print("[0] Sair da conversa com o tarveneiro")
                print("[1] Comprar Suprimentos -> $" + str(valorSuprimento))
                print("[2] Restaurar a Sanidade com uma cerveja amanteigada -> $" + str(valorSanidade))
                print("[3] Aumentar os espaço dos items em 2 unidades")
                print("[4] Aumentar os espaço dos iventário em 5 unidades")
                print(16*"-")
                print(f'Ouro: {personagem["ouro"]} | Hp: ({personagem["hp"]} \ {personagem["vida"]}) \nSuprimentos: ({personagem["suprimentos_complementar"]} / {personagem["suprimentos"]}) | Sanidade: ({personagem["sanidade_complementar"]} / {personagem["sanidade"]})')                
                print(16*"-")
        
                try:
                    opcao_conversa = int(input("Entrada > "))
                except ValueError:
                    print("Entrada inválida!")
                    continue
                
                if opcao_conversa == 0:
                    os.system("clear")
                    print("Saindo da conversa com o tarveneiro...")
                    break
                elif opcao_conversa == 1:
                    if personagem["ouro"] >= valorSuprimento:
                        personagem["ouro"] -= valorSuprimento
                        personagem["suprimentos_complementar"] = personagem['suprimentos']
                        print(f"\nVocê comprou suprimentos por ${valorSuprimento}!")
                    else:
                        print("\nVocê não tem ouro suficiente para comprar suprimentos.")
                
                elif opcao_conversa == 2:
                    if personagem["ouro"] >= valorSanidade:
                        personagem["ouro"] -= valorSanidade
                        personagem["sanidade_complementar"] = personagem['sanidade']
                        print("\nVocê bebe uma cerveja amanteigada e sente sua sanidade se restaurar.")
                    else:
                        print("\nVocê não tem ouro suficiente para comprar uma cerveja amanteigada.")
                    
                elif opcao_conversa == 3:
                    print("\nVocê conversa sobre suas aventuras e o tarveneiro decide aumentar o espaço dos seus items em 2 unidades.")
                    
                elif opcao_conversa == 4:
                    print("\nO tarveneiro, impressionado com suas histórias, decide aumentar o espaço do seu iventário em 5 unidades.")
                    
                else:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
                    
        elif opcao == 2:
            print("\nVocê sobe para o quarto e consegue descansar um pouco.")
            personagem["hp"] = int(personagem["vida"])  # Recupera toda a vida
            print("Sua vida foi completamente restaurada! Hp: (" + str(personagem["hp"]) + " / " + str(personagem["vida"]) + ")")
            
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
            
    return personagem, controle1

def suprimento_complementar(personagem):
    if personagem['suprimentos'] <= 32:
        calcularValorSuprimento = int((1 - (int(personagem['suprimentos_complementar'])/int(personagem['suprimentos']))) * 64)
    elif personagem['suprimentos'] > 32 and personagem['suprimentos'] <= 64:
        calcularValorSuprimento = int((1 - (int(personagem['suprimentos_complementar'])/int(personagem['suprimentos']))) * 128)
    elif personagem['suprimentos'] > 64 and personagem['suprimentos'] <= 128:
        calcularValorSuprimento = int((1 - (int(personagem['suprimentos_complementar'])/int(personagem['suprimentos']))) * 256)
    elif personagem['suprimentos'] > 128 and personagem['suprimentos'] <= 256:
        calcularValorSuprimento = int((1 - (int(personagem['suprimentos_complementar'])/int(personagem['suprimentos']))) * 512)
        
    return calcularValorSuprimento

def sanidade_complementar(personagem):
    if personagem['sanidade'] <= 10:
        calcularValorSanidade = int((1 - (int(personagem['sanidade_complementar'])/int(personagem['sanidade']))) * 16)
    elif personagem['sanidade'] > 10 and personagem['sanidade'] <= 20:
        calcularValorSanidade = int((1 - (int(personagem['sanidade_complementar'])/int(personagem['sanidade']))) * 32)
    elif personagem['sanidade'] > 20 and personagem['sanidade'] <= 30:
        calcularValorSanidade = int((1 - (int(personagem['sanidade_complementar'])/int(personagem['sanidade']))) * 64)
    elif personagem['sanidade'] > 30 and personagem['sanidade'] <= 50:
        calcularValorSanidade = int((1 - (int(personagem['sanidade_complementar'])/int(personagem['sanidade']))) * 128)
    elif personagem['sanidade'] > 50 and personagem['sanidade'] <= 80:
        calcularValorSanidade = int((1 - (int(personagem['sanidade_complementar'])/int(personagem['sanidade']))) * 256)
    elif personagem['sanidade'] > 80 and personagem['sanidade'] <= 130:
        calcularValorSanidade = int((1 - (int(personagem['sanidade_complementar'])/int(personagem['sanidade']))) * 512)
        
    return calcularValorSanidade

    