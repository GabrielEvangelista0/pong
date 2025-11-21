import pygame
from Bola import Bola
from Raquete import Raquete
from Evento import ProcssarEventos

pygame.init()
width, heigth = 800, 600
pygame.display.set_caption("jogo de pong")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, heigth))

bola = Bola(width/2, heigth/2, 10)
jogador1 = Raquete(width/2, heigth - 30, 100, 10)
cpu = Raquete(width/2, 30, 100, 10)
input_handler = ProcssarEventos(jogador1, cpu, bola)
cor = (255,255,255)

rodando = True

while rodando:
    clock.tick(120)
    rodando = input_handler.processar_eventos()
    screen.fill((0,0,0))
    bola.moverBola()
    bola.verificaColizao(jogador1)
    bola.verificaColizao(cpu)
    pygame.draw.rect(screen, cor, (cpu.x, cpu.y, cpu.width, cpu.heigth), 0)
    pygame.draw.rect(screen, cor, (jogador1.x, jogador1.y, jogador1.width, jogador1.heigth), 0)
    pygame.draw.circle(screen, cor, (bola.x, bola.y), bola.r)
    pygame.display.flip()

pygame.quit()