class Animal:
    def __init__(self) -> None:
        print("animal creado")
    
        self.vertebrado = False
        self.mamifero = False
        self.patas = 4
        self.ojos = 2     
        self.pelaje = False
    
    def nacimiento(self):
        pass
    
    def comida(self):
        print("ya comi we")
    
    def desplazamiento(self):
        pass
        

class Tiburon(Animal):
    def __init__(self):
        super().__init__()
        print("tiburon creado")

        self.vertebrado = True
        self.mamifero = False
        self.patas = 0
        self.ojos = 2     
        self.pelaje = False
        
    def Nadar(self):
        print("nadaremos, nadaremos")


class TiburonBlanco(Tiburon):
    def __init__(self):
        super().__init__()
        print("Tiburon blanco creado")

class TiburonBallena(Tiburon):
    def __init__(self):
        super().__init__()
        print("Tiburon va llena creado")

class TiburonMartillo(Tiburon):
    def __init__(self):
        super().__init__()
        print("tiburon martillo creado")

print("/////////////////")

class Perro(Animal):
    def __init__(self):
        super().__init__()
        print("perro creado")

        self.vertebrado = True
        self.mamifero = True
        self.patas = 4
        self.ojos = 2     
        self.pelaje = True
        
    def ladrar(self):
        print("ladrando")   
        
class Golden(Perro):
    def __init__(self):
        super().__init__()
        print("perrito golden creado")

class Husky(Perro):
    def __init__(self):
        super().__init__()
        print("perrito husky creado")

class caniche(Perro):
    def __init__(self):
        super().__init__()
        print("perrito caniche creado")

print("/////////////////")
ListaAnimales = [TiburonBallena(), TiburonBlanco(), TiburonMartillo(), Husky(), Golden(), caniche()]

print("/////////////////")
for comer in ListaAnimales:
    print(f"\nEvaluando a: {type(comer).__name__}")
    comer.comida()