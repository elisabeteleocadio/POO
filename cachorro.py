class Cachorro:
    def _init_(self, nome, raca, comida):
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.acordado = False
        self.feliz = False
        
def comer(self):
    if self.comida>0:
        self.comida-=1
        self.feliz= True
        return f"{self.nome} comeu e está feliz!!"
    return f"{self.nome} está sem comida!"
def dormir(self): 
    self.acordado = False
    return f"{self.nome}dormindo"
def acordar(self):
    self.acodado = True
    return f"{self.nome} está acordado!"
def brincar (self):
    self.feliz= True
    return f"{self.nome} está brincando feliz!"
def ignorar (self):
    self.feliz = False
    return f"{self.nome} está triste porque foi ignorado."
def latir (self):
    if self.acordado: 
        return f"{self.nome} está latindo: au au au!!!"
    return f"{self.nome} está dormindo e não pode latir."

#Criação dos cachorros:


Wille = Cachorro ("Wilee", "Poodle", 3) 
 