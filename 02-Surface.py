import pygame, psutil

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo de Surface')
azul = (0, 0, 255)

pygame.display.init()

s1 = pygame.surface.Surface((largura, altura/3)) # medida total
s2 = pygame.surface.Surface((largura, altura/3))
s3 = pygame.surface.Surface((largura, altura/3))

pygame.draw.rect(s1, azul, (20, 50, largura - 2*20, 70))
tela.blit(s1, (0,0))
pygame.draw.rect(s2, azul, (20, 50, largura - 2*20, 70))
tela.blit(s1, (0,altura/3))
pygame.draw.rect(s3, azul, (20, 50, largura - 2*20, 70))
tela.blit(s1, (0,2*altura/3))

clock = pygame.time.Clock()

terminou = False
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                terminou = True

    pygame.display.update()

    clock.tick(60)

pygame.display.quit()

