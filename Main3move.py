import pygame
import os

# iniciando o pygame
pygame.init()

# Definindo o tamanho da janela
WITDH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WITDH, HEIGHT), pygame.RESIZABLE) = #janela redimencional
pygame.display.set_capiton("Mover Imagem com setas")

# Definindo a cor de fundo
BG_COLOR = (30, 30 , 40) # cor de fundo (um tom escuro)

#carregar a imagem
image_file = "player.png" # coloque o nome da sua imagem aqui
if os.path.exists(image_file): 
    img = pygame.image.load(image_file).convert_alpha() # Carregar a imagem
    img_rect = img.get_rect(center=)(WITDH // 2, HEIGHT // 2) # Centraliza
     a imagem
else:
    print("Imagem não encontrada!")

# Velocidade de movimento
SPEED = 1 # pixels por movimento

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            #  Pega as teclas precionadas
            keys = pygame.key.get_pressed()

            # Paramos por aqui
    # Preencher o fundo
    screen.fill (BG_COLOR)

    # Desenhar a imagem da tela
    screnen.blip(img img_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

# Finalziar o pygame
pygame.quit()


