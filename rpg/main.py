from funcoes import criar_guerreiro,criar_ladino,criar_mago,criar_paladino
from Especies import *

print("Bem vindo(a)! Selecione a raça de seu personagem:\n")

profissao = {
    "1" : [criar_guerreiro(), "Guerreiro"],
    "2" : [criar_ladino(),"Ladino"],
    "3" : [criar_mago(),"Mago"],
    "4" : [criar_paladino(),"Paladino"]
}

raca = {
    "1" : [Humano(), "Humano"],
    "2" : [Elfo(), "Elfo"],
    "3" : [Anao(), "Anão"],
    "4" : [Ciclope(), "Ciclope"]
}

opcoes = ("1","2","3","4","5")

while True:
    escolha = input("(1) Humano\n(2) Elfo\n(3) Anão\n(4) Ciclope\n(5) Sair\n\n")
    if not escolha in opcoes:
        print("Escolha uma opção válida!\n")
    elif escolha == "5":
        print("Volte sempre!\n")
        break
    else:
        persona = raca[escolha][0]
        print(persona.__dict__)
        break

print(f"\nCerto, voce será da raça {raca[escolha][1]}.\n")
print("Agora escolha sua classe:\n")

while True:
    escolha = input("(1) Guerreiro\n(2) Ladino\n(3) Mago\n(4) Paladino\n(5) Sair\n\n")
    if not escolha in opcoes:
        print("Escolha uma opção válida!\n")
    elif escolha == "5":
        print("Volte sempre!\n")
        break
    else:
        profissao[escolha][0]
        print(persona.__dict__)
        break
    
print(f"\nCerto, voce será da classe {profissao[escolha][1]}.\n")