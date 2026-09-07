class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def perimetro(self):
        "calcula el perimetro del rectangulo"
        return 2 * (self.ancho + self.alto)

    def area(self):
        "calcula el area de un rectangulo"
        return self.ancho * self.alto

    def identificarse(self):
        return "Hola, soy un rectangulo"

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def identificarse(self):
        return "Hola, soy un cuadrado"

r1 = Rectangulo(5, 2)
c1 = Cuadrado(5)
print(f"{r1.identificarse()} - Perimetro: {r1.perimetro()} - Area: {r1.area()}")
print(f"{c1.identificarse()} - Perimetro: {c1.perimetro()} - Area: {c1.area()}")

