import pygame
from Raquete import Raquete

class Bola:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 2
        self.vy = 3
        pass

    def moverBola(self):
        self.x += self.vx
        self.y+= self.vy
        if self.x <= 15 or self.x >= 800 - 10:
            self.vx = -self.vx
    
        if self.y <= 15 or self.y >= 600 - 10:
            self.vy = -self.vy

    def verificaColizao(self, raquete):
        # raquete tem atributos: x, y, width, heigth
        # calcula o ponto do retângulo mais próximo do centro da bola
        nearest_x = max(raquete.x, min(self.x, raquete.x + raquete.width))
        nearest_y = max(raquete.y, min(self.y, raquete.y + raquete.heigth))

        dx = self.x - nearest_x
        dy = self.y - nearest_y

        # colisão se a distância ao quadrado <= r^2
        if dx*dx + dy*dy <= (self.r * self.r):
            # reflita a velocidade vertical (vai para cima da raquete)
            self.vy = -abs(self.vy)

            # evita que a bola fique "presa" movendo-a para fora da raquete
            dist = (dx*dx + dy*dy) ** 0.5 or 1
            overlap = self.r - dist
            if overlap > 0:
                self.x += (dx / dist) * overlap
                self.y += (dy / dist) * overlap

            # opcional: variar vx conforme o ponto de impacto para controle de ângulo
            hit_pos = (self.x - (raquete.x + raquete.width / 2)) / (raquete.width / 2)
            self.vx += hit_pos * 2  # ajuste fino conforme desejado