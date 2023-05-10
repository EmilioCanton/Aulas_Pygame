import pygame, sys
from pygame.locals import *

pygame.init()

# Configura a janela
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# Configura as cores, com o codigo RGB
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

# Desenha na superficie
DISPLAYSURF.fill(WHITE)
# DISPLAYSURF.fill(RGB)

# Pentagono verde
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277),(56, 277), (0, 106)))

# pygame.draw.polygon(Superficie, Cor, Arestas, Largura') -> Largura é opcional, default = 0


# Linha superior do desenho da letra Z
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60),4)
# pygame.draw.line(Superficie, Cor, Inicio, Final, Largura') -> Largura é opcional, default = 1

# Linha do corpo da letra Z
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
# Linha inferior do desenho da letra Z

pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)

# Circulo azul preenchido
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
# pygame.draw.circle(Superficie, Cor, Ponto_Central, Raio, Largura') -> Largura é opcional, default = 0


# Desenho ovalado com interior vazio
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
# pygame.draw.ellipse(Superficie, Cor, Retangulo_Borda, Largura') -> Largura é opcional, default = 0

# Retangulo vermelho
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50)) 
# pygame.draw.rect(Superficie, Cor, Tupla_Retangulo, Largura') -> Largura é opcional, default = 0

# Pontinhos pretos no canto inferior direito
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK

del pixObj

# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT: # Caso o X da janela seja selecionado
            pygame.quit()
            sys.exit()
    pygame.display.update()
