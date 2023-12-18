from funcoes import criar_guerreiro, criar_ladino, criar_mago, criar_paladino
from Especies import *
from detalhes import *
from tkinter import *
from tkinter.ttk import *

racas = ("Humano", "Elfo", "Anão", "Meio-orc")
classes = ("Guerreiro", "Ladino", "Mago", "Paladino")

janela = Tk()
janela.geometry("950x650")
Checkbutton1 = IntVar()
# imagens -------------------------------------------------------------------

logo = PhotoImage(file="rpg\\imagens\\logo@0.75x.gif")
titulo = Label(janela, image=logo)
imagem = Label(janela)
vida_desc = Label(janela, text="VIDA : ", font="Arial 12")
mana_desc = Label(janela, text="MANA : ", font="Arial 12")
vida = Progressbar(janela, length=300, value=100, mode="determinate")
mana = Progressbar(janela, length=300, value=100, mode="determinate")

# escritos ------------------------------------------------------------------

nome_info = Label(janela, text="Nome do Personagem", font="Arial 15")
nome = Entry(janela, width=30, font="Arial 12")
raca_info = Label(janela, text="Selecione sua raça", font="Arial 15")
raca = Combobox(janela, values=racas, font="Arial 12")
classe_info = Label(janela, text="Selecione sua classe", font="Arial 15")
classe = Combobox(janela, values=classes, font="Arial 12")
sexo = Label(janela, text="Selecione seu sexo", font="Arial 15")


# poscicoes -----------------------------------------------------------------

titulo.pack()
nome_info.place(x=600, y=100)
nome.place(x=600, y=130)
raca_info.place(x=600, y=160)
raca.place(x=600, y=190)
classe_info.place(x=600, y=220)
classe.place(x=600, y=250)
imagem.place(x=600, y=310)
vida.place(x=100, y=130)
mana.place(x=100, y=190)
vida_desc.place(x=100, y=100)
mana_desc.place(x=100, y=160)


fotos_masc = {
    "Guerreiro": PhotoImage(file="rpg\\imagens\\guerreiro.gif"),
    "Ladino": PhotoImage(file="rpg\\imagens\\ladino.gif"),
    "Mago": PhotoImage(file="rpg\\imagens\\mago.gif"),
    "Paladino": PhotoImage(file="rpg\\imagens\\paladino.gif")
}
fotos_fem = {
    "Guerreiro": PhotoImage(file="rpg\\imagens\\guerreira.gif"),
    "Ladino": PhotoImage(file="rpg\\imagens\\ladina.gif"),
    "Mago": PhotoImage(file="rpg\\imagens\\maga.gif"),
    "Paladino": PhotoImage(file="rpg\\imagens\\paladina.gif")
}

def selecao_masc():
        choice = classe.get()
        imagem.configure(image=fotos_masc[choice])
def selecao_fem():
        choice = classe.get()
        imagem.configure(image=fotos_fem[choice])


# botao_del = Button(janela, text="trocar", command=selecao)
# botao_del.place(x=475, y=100)
botato_masc = Radiobutton(janela, text="Masculino", variable=Checkbutton1, value=1, command=selecao_masc)
botato_fem = Radiobutton(janela, text="Feminino", variable=Checkbutton1, value=2, command=selecao_fem)
botato_masc.place(x=600, y=280)
botato_fem.place(x=700, y=280)



janela.mainloop()
