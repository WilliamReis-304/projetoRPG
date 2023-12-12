from Especies import *

def criar_guerreiro(a):
    a.forca += 2
    a.defesa += 1
    a.agilidade -= 1
    a.magia -= 1
    # maestria = True
    
def criar_ladino(a):
    a.agilidade += 2
    a.destreza += 3
    # furtividade = True
    
def criar_mago(a):
    a.forca -= 1
    a.inteligencia += 2
    a.magia += 3
    # magia_inicial = True
    
def criar_paladino(a):
    a.forca += 2
    a.defesa += 3
    a.magia += 2
    # reza = True