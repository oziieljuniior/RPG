from Jogo.Configuracoes.AtualizarDescricao import atualizar_json
from Jogo.Raizes.mapa import mapa
from Jogo.Eventos.dia import eventodialooper
from Jogo.Eventos.sorte import rollSorte
import os # os.system("clear")
from Jogo.Raizes.cuiafurada import cuiafurada
from Jogo.Raizes.adega import adega
from Jogo.Raizes.teatroAmazonas import teatro
from Jogo.Raizes.campoTreinamento import campo
from Jogo.Raizes.sortimentosVariados import sortimentos
from Jogo.Raizes.ferreiro import ferreiro
from Jogo.Raizes.caldeirao import caldeirao
from Jogo.Raizes.diario import diario

def iniciar_jogo(usuario, personagem):
    controle1 = 0
    while True:
        print("\n==============================")
        print("🎮 AVENTURA - Cidade de Manaus")
        print(f"Jogador: {usuario}")
        print(f"Personagem: {personagem['nome']} ({personagem['classe']})")
        print(f'Nível: {personagem['nivel']} (xp {personagem['xp']} / {personagem['xp_complementar']})')
        print(f'Dia: {personagem['dia']}')
        print("==============================")
        
        print("\nEvento Dia")
        
        eventodialooper(personagem)
        
        if controle1 == 0:
            personagem['sorte'] = rollSorte()
            controle1 = 1
            
        print("\n=== TELA DO JOGO ===")
        
        print("[1] Cuia Furada")
        print("[2] Adega")
        print("[3] Teatro Amazonas")
        print("[4] Personagem")
        print("[5] Campos de Treinamento")
        print("[6] Sortimentos Variados")
        print("[7] Ferreiro")
        print("[8] Caldeirão Borbulhante")
        print("[9] Diário")
        print("[10] Mapa")
        print("[11] Salvar e Sair")

        try:
            opcao = int(input("Entrada > "))
        except ValueError:
            print("Entrada inválida!")
            continue

        if opcao == 1:
            os.system("clear")
            print(16*'-*')
            print("Cuia Furada - Local de encontros e eventos sociais.")
            personagem, controle1 = cuiafurada(personagem, controle1)
            
        elif opcao == 2:
            os.system("clear")
            print(16*'-*')
            print("Adega - Local para aumentar suas habilidades de combate.")
            adega(personagem)
            
        elif opcao == 3:
            os.system("clear")
            print(16*'-*')
            print("Teatro Amazonas - Local para eventos culturais e artísticos.")
            teatro(personagem)
            
        elif opcao == 4:
            os.system("clear")
            print("\n========= STATUS =========")
            for chave, valor in personagem.items():
                print(f"{chave.capitalize()}: {valor}")
            
        elif opcao == 5:
            os.system("clear")
            print(16*'-*')
            print("Campos de Treinamento - Local para aprimorar suas habilidades.")
            campo(personagem)
            
        elif opcao == 6:
            os.system("clear")
            print(16*'-*')
            print("Sortimentos Variados - Local para comprar itens e equipamentos.")
            sortimentos(personagem)
        
        elif opcao == 7:
            os.system("clear")
            print(16*'-*')
            print("Ferreiro - Local para forjar equipamentos.")
            ferreiro(personagem)
            
        elif opcao == 8:
            os.system("clear")
            print(16*'-*')
            print("Caldeirão Borbulhante - Local para preparar poções e elixires.")
            caldeirao(personagem)
            
        elif opcao == 9:
            os.system("clear")
            print(16*'-*')
            print("Diário - Registros de eventos e missões.")
            diario(personagem)
            
        elif opcao == 10:
            os.system("clear")
            print(16*'-*')
            print("Mapa - Visualização do mapa da cidade.")
            mapa(personagem)
            
        
        elif opcao == 11:
            print("Salvando progresso...")
            atualizar_json(personagem)
            os.system("clear")
            break
        else:
            print("Opção inválida!")
