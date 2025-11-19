import pygame
from Raquete import Raquete

class ProcssarEventos:
    def __init__(self, jogador):
        # O Handler precisa conhecer o player para mandar comandos a ele
        self.jogador = jogador

    def processar_eventos(self):
        for event in pygame.event.get():
            # Evento de fechar a janela
            if event.type == pygame.QUIT:
                return False
            
        
        keys = pygame.key.get_pressed()
           
        if keys[pygame.K_LEFT]:
            self.jogador.moverRaqueteparaEsquerda()

        if keys[pygame.K_RIGHT]:
            self.jogador.moverRaqueteparaDireita()
    

        return True