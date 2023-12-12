from Especies import *

persona = Especies(0,0,0,0,0,0,0,0)

def criar_guerreiro():
    persona.forca = persona.forca + 3
    persona.defesa = persona.defesa + 2
    persona.agilidade = persona.agilidade - 1
    persona.magia = persona.magia - 1
    # maestria = True
    
def criar_ladino():
    persona.agilidade = persona.agilidade + 2
    persona.destreza = persona.destreza + 3
    persona.magia = persona.magia + 1
    # furtividade = True
    
def criar_mago():
    persona.forca = persona.forca - 1
    persona.inteligencia = persona.inteligencia + 1
    persona.magia = persona.magia + 3
    # magia_inicial = True
    
def criar_paladino():
    persona.forca = persona.forca + 2
    persona.defesa = persona.defesa + 3
    persona.magia = persona.magia + 2
    persona.inteligencia = persona.inteligencia +1
    # reza = True