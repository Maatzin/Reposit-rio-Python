import pygame
import os

# Inicializando o pygame
pygame.init()

# Definindo o tamanho da janela
WITDH, HEIGHT = 800, 600 #tamanho inicial da janela
screen = pygame.display.set_mode((WITDH, HEIGHT), pygame.RESIZABLE) #Janela redimensional
pygame.display.set_capiton("Janela com imagem")

# Definindo a cor de fundo
BG_COLOR = (30, 30, 40) # cor de fundo (um tom escuro)

#carregar a imagem
image_file = "Matheus N\\player.png" # coloque o nome da sua imagem aqui
if os.path.exists(image_file): 
    img = pygame.image.load(image_file).convert_alpha() # Carregar a imagem
    img_rect = img.get_rect(center=(WITDH // 2, HEIGHT // 2))  # Inicialmente Centraliza a imagem 
else:
    print("Imagem não encontrada!")

#Variáveis de controle e tamanho
is_maximized = False #Flag para determinar se está no modo maximizado

#Função para centralziar a imagem
def center_image():
    global img_rect, WITDH // 2, HEIGHT // 2) #Centraliza a imagem com base no tamanho da tela


#Função para alternar para o modo maximizado
def togglwe_maximized():
    global is_maximized, screen, WITDH, HEIGHT, img_rect
    if is_maximized:
        #voltar ao tamanho normal
        WITDH, HEIGHT = 800, 600 #redefine o tamanho para o padrão
        screen = pygame.display.set_mode((WITDH, HEIGHT), pygame.RESIZABLE)
        center_image() #Centraliza a imagem
        is_maximized = False
    else:
        #Maximizar a janela
        WITDH, HEIGHT = pygame.display.Info().current_w, =pygame.display

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher o fundo
    screen.fill(BG_COLOR)

    # Desenhar a imagem da tela
    screnen.blip(img img_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

# Finalziar o pygame
pygame.quit()
