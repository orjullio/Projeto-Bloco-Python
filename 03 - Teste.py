import pygame, psutil

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo de Surface')
azul = (0, 0, 255)

pygame.display.init()

s1 = pygame.surface.Surface((largura, altura / 3)) # Dimensão da superfície onde vai rolar.

pygame.draw.rect(s1, azul, largura - 2*20, 50)



clock = pygame.time.Clock()

terminou = False
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                terminou = True

    pygame.display.update()

    clock.tick(60)

pygame.display.quit()

