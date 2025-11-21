import pygame

class Raquete:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        pass

    def moverRaqueteparaEsquerda(self):
        self.x -= 5
        print(self.x)
        if self.x < 0:
            self.x = 0

    def moverRaqueteparaDireita(self):
        self.x += 5
        print(self.x)
        if self.x > 800 - self.width:
            self.x = 800 - self.width