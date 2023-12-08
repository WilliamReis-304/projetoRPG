from Classes import *
from funcoes import *


classe = {
    "1" : criar_guerreiro(),
    "2" : criar_ladino(),
    "3" : criar_mago(),
    "4" : criar_paladino()
    }
opcoes = ("1","2","3","4","5")

while True:
    print("Qual classe deseja usar?\n")
    persona = input("(1) Guerreiro\n(2) Ladino\n(3) Mago\n(4) Paladino\n(5) Sair\n")
    if not persona in opcoes:
        print("\nPor favor escolha ima das opções exibidas!\n")
    else:
        if persona == "5":
            print("Volte logo!")
        else:
            player = classe[persona]
        break
print(f"Certo então você escolheu a classe {type(player)} e seus atributos são:")
print(player.__dict__)