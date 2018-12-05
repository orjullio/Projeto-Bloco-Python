import pygame, psutil

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Uso de memória')
preto = (0,0,0)
azul = (0,0,255)
vermelho = (255,0,0)
branco = (255,255,255)


pygame.font.init()
font = pygame.font.Font(None, 32)
cont = 60

s1, s2, s3 = [pygame.surface.Surface((largura, altura/3))] *3

# tela.blit(esp1, (0,0))
# tela.blit(esp2, (0, altura / 3))
# tela.blit(esp3, (0, 2 * altura / 3))

clock = pygame.time.Clock()



terminou = False

def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura - 2*20
    tela.fill(preto)
    s1.fill(azul, (20, 50, larg, 70))
    larg = larg*mem.percent/100
    s1.fill(vermelho, (20, 50, larg, 70))
    total = round(mem.total/(1024*1024*1024), 2)
    texto_barra = 'Uso memória (Total: {}GB):'.format(total)
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))




def mostra_uso_cpu():
    tela.blit(esp1, (0, altura/3))
    capacidade = psutil.cpu_percent(interval=0)
    larg = largura - 2*20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg*capacidade/100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    text = font.render('Uso de CPU: ', 1, branco)
    tela.blit(text, (20, 10))

def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura - 2 * 20
    tela.fill(preto)
    pygame.draw.rect(tela, azul, (20, 50, larg, 70))
    larg = larg * disco.percent / 100
    pygame.draw.rect(tela, vermelho, (20, 50, larg, 70))
    total = round(disco.total / (1024 * 1024 * 1024), 2)
    texto_barra = 'Uso Total de Disco: {}GB'.format(total)
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))


while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    if cont == 60:
        mostra_uso_memoria()
        cont = 0

    pygame.display.update()

    clock.tick(60)
    cont += 1

pygame.display.quit()
