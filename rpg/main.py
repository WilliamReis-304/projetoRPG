from funcoes import criar_guerreiro,criar_ladino,criar_mago,criar_paladino
from Especies import *
from detalhes import *

print("Bem vindo(a)! Selecione a raça de seu personagem:\n")


raca = {
    "1" : [Humano(), "Humano"],
    "2" : [Elfo(), "Elfo"],
    "3" : [Anao(), "Anão"],
    "4" : [Meio_Orc(), "Meio-Orc"]
}

opcoes = ("1","2","3","4","5")

while True:
    detalhe_raca()
    escolha = input("(1) Humano\n(2) Elfo\n(3) Anão\n(4) Ciclope\n(5) Sair\n\n")
    if not escolha in opcoes:
        print("Escolha uma opção válida!\n")
    elif escolha == "5":
        print("\nVolte sempre!\n")
        exit()
    else:
        persona = raca[escolha][0]
        print(persona.__dict__)
        print(f"\nCerto, voce será da raça {raca[escolha][1]}.\n")
        break

profissao = {
    "1" : [criar_guerreiro(persona), "Guerreiro"],
    "2" : [criar_ladino(persona),"Ladino"],
    "3" : [criar_mago(persona),"Mago"],
    "4" : [criar_paladino(persona),"Paladino"]
}

print("Agora escolha sua classe:\n")

while True:
    detalhe_classe()
    escolha = input("(1) Guerreiro\n(2) Ladino\n(3) Mago\n(4) Paladino\n(5) Sair\n\n")
    if not escolha in opcoes:
        print("Escolha uma opção válida!\n")
    elif escolha == "5":
        print("\nVolte sempre!\n")
        exit()
    else:
        profissao[escolha][0]
        print(persona.__dict__)
        print(f"\nCerto, voce será da classe {profissao[escolha][1]}.\n")
        break
    