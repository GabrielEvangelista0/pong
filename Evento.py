import pygame
from Raquete import Raquete

class ProcssarEventos:
    def __init__(self, jogador, cpu, bola):
        # O Handler precisa conhecer o player para mandar comandos a ele
        self.jogador = jogador
        self.cpu = cpu
        self.bola = bola
    def processar_eventos(self):
        for event in pygame.event.get():
            # Evento de fechar a janela
            if event.type == pygame.QUIT:
                return False
            
        self.moveJogador()
        self.moverCPU(self.cpu, self.bola)
        return True
    
    def moveJogador(self):
        keys = pygame.key.get_pressed()
           
        if keys[pygame.K_LEFT]:
            self.jogador.moverRaqueteparaEsquerda()

        if keys[pygame.K_RIGHT]:
            self.jogador.moverRaqueteparaDireita()

    def moverCPU(self, cpu, bola):
        # Simples IA para mover a raquete da CPU em direção à bola
        if bola.x < cpu.x + cpu.width / 2:
            cpu.moverRaqueteparaEsquerda()
        elif bola.x > cpu.x + cpu.width / 2:
            cpu.moverRaqueteparaDireita()
        elif bola.x == cpu.x + cpu.width / 2:
            pass