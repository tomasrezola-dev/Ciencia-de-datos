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

r1 = Rectangulo(5, 2)
print(f"Perimetro: {r1.perimetro()} - Area: {r1.area()}")

