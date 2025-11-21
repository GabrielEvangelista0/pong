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
        # Assumindo atributos: self.x, self.y, self.r, self.vx, self.vy
        # e raquete.x, raquete.y, raquete.width, raquete.heigth
        nearest_x = max(raquete.x, min(self.x, raquete.x + raquete.width))
        nearest_y = max(raquete.y, min(self.y, raquete.y + raquete.heigth))

        dx = self.x - nearest_x
        dy = self.y - nearest_y
        dist2 = dx*dx + dy*dy

        if dist2 <= (self.r * self.r):
            # evita divisão por zero
            dist = dist2 ** 0.5 or 1.0
            nx = dx / dist
            ny = dy / dist

            # refletir velocidade na normal n = (nx, ny)
            v_dot_n = self.vx * nx + self.vy * ny
            self.vx = self.vx - 2 * v_dot_n * nx
            self.vy = self.vy - 2 * v_dot_n * ny

            # empurra a bola para fora do retângulo para evitar ficar presa
            overlap = self.r - dist
            if overlap > 0:
                self.x += nx * overlap
                self.y += ny * overlap
            
            #variar vx conforme o ponto de impacto para controle de ângulo
            hit_pos = (self.x - (raquete.x + raquete.width / 2)) / (raquete.width / 2)
            self.vx += hit_pos * 1.5  # ajuste fino conforme desejado

            #pequeno aumento de velocidade para variar o jogo
            self.vx *= 1.02
            self.vy *= 1.02