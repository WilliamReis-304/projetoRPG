class Classes:
    def __init__(self, forca : int, destreza: int, agilidade : int, defesa : int, magia : int, inteligencia : int):
        self.forca = forca
        self.destreza = destreza
        self.agilidade = agilidade
        self.defesa = defesa
        self.magia = magia
        self.inteligencia = inteligencia

class Guerreiro(Classes):
    def __init__(self):
        super().__init__(2,2,2,2,2,2)
        self.forca = self.forca + 3
        self.defesa = self.defesa + 2
        self. agilidade = self.agilidade - 1
        self.magia = self.magia - 1
    
    def maestria():
        return True

class Ladino(Classes):
    def __init__(self):
        super().__init__(2,2,2,2,2,2)
        self.agilidade = self.agilidade + 2
        self.destreza = self.destreza + 3
        self.magia = self.magia + 1

    def furtividade():
        return True

class Mago(Classes):
    def __init__(self):
        super().__init__(2,2,2,2,2,2)
        self.forca = self.forca - 1
        self.inteligencia = self.inteligencia + 1
        self.magia = self.magia + 3

    def magia_inicial():
        return True

class Paladino(Classes):
    def __init__(self):
        super().__init__(2,2,2,2,2,2)
        self.forca = self.forca + 2
        self.defesa = self.defesa + 3
        self.magia = self.magia + 2
        self.inteligencia = self.inteligencia +1

    def reza():
        return True