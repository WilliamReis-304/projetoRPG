class Especies:
    def __init__(self, vida: int, mana : int, forca : int, destreza: int, agilidade : int, defesa : int, magia : int, inteligencia : int):
        self.forca = forca
        self.destreza = destreza
        self.agilidade = agilidade
        self.defesa = defesa
        self.magia = magia
        self.inteligencia = inteligencia
        self.vida = vida
        self.mana = mana

class Elfo(Especies):
    def __init__(self):
        super().__init__(20, 10, 2, 2, 2, 2, 2, 2)
        self.magia += 2
        self.inteligencia += 3
        self.destreza +=1

class Humano(Especies):
    def __init__(self):
        super().__init__(30, 5, 2, 2, 2, 2, 2, 2)
        self.magia += 1
        self.inteligencia += 1
        self.defesa +=1
        self.forca +=1
        self.destreza +=1
        self.agilidade +=1

class Meio_Orc(Especies):
    def __init__(self):
        super().__init__(40, 3, 2, 2, 2, 2, 2, 2)
        self.magia -= 1
        self.inteligencia -= 1
        self.defesa += 4
        self.forca += 3

class Anao(Especies):
    def __init__(self):
        super().__init__(35, 3, 2, 2, 2, 2, 2, 2)
        self.defesa +=2
        self.forca +=3

# class Goblin(Especies):
#     def __init__(self):
#         super().__init__(15, 0, 2, 2, 2, 2, 2, 2)
#         self.magia += 1
#         self.inteligencia += 1
#         self.defesa +=1
#         self.forca +=1
#         self.destreza +=1
#         self.agilidade +=1
        
# class Zumbi(Especies):
#     def __init__(self):
#         super().__init__(20, 0, 2, 2, 2, 2, 2, 2)
        
# class Pantera(Especies):
#     def __init__(self):
#         super().__init__(30, 0, 2, 2, 2, 2, 2, 2)
        

