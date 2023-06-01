import sys, pygame
from pygame.locals import *
from random import *

clock = pygame.time.Clock()

# definir a classe da imagem
class Imagem(pygame.sprite.Sprite):
    def __init__(self, imagem_arquivo, posicao, velo):
        super().__init__()
        self.image = imagem_arquivo
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = posicao
        self.velocidade = velo

    def update(self):
        self.rect.move_ip(self.velocidade)

        if self.rect.left < 0 or self.rect.right > largura:
            self.velocidade[0] = -self.velocidade[0]
        if self.rect.top < 0 or self.rect.bottom > altura:
            self.velocidade[1] = -self.velocidade[1]

# classe botao
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

    #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

# definir função som
def Tocar(som):
    if tocar_som == True: som.play()

# def função mutar
def mute():
    global tocar_som
    if tocar_som == True:
        tocar_som = False
        volume = Button(740, 5, volume_imagem_mudo, 1)

def unmute():
    global tocar_som
    if tocar_som == False:
        tocar_som = True
        volume = Button(740, 5, volume_imagem, 1)

# Função para desenhar o ranking
def desenhar_ranking():
    texto_titulo = font.render("RANKING DE JOGADORES", True, YELLOW)
    tela.blit(texto_titulo, (20,10))
    posicao_y = 72
    for i, jogador in enumerate(jogadores):
        posicao = i + 1
        texto_jogador = font.render(f"#{posicao} {jogador} - {scores[i]}", True, BLACK)
        tela.blit(texto_jogador, (20, posicao_y))
        posicao_y += 40

# inicializar o Pygame
pygame.init()

# Cores
BLACK  = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (170, 255, 0)
RED = (238, 75, 43)
ORANGE = (255,140,0)

# definir a largura e altura da janela
largura, altura = 800, 600
size = (largura, altura)

# Declarando variável
font = pygame.font.SysFont('verdana',35)
pontos = 0
vidas = 5
count_personagem = 1
count_personagem_menu = 1
imagem_personagem = 1
imagem_personagem_menu = 1
inverter_fundo = 0
flag_fundo = 0
pode_atacar = True
tocar_som = True
largura_botao, altura_botao = 50, 50
CLOCK = 60
tempo = 20
temporizador = tempo
menu_var = 1
fase = 1
instrucao_flag = 0


title_text = font.render("Fúria Natural: A Jornada dos Três Desastres", True, WHITE)
button1_text = font.render("Jogar", True, WHITE)
button2_text = font.render("Instruções", True, WHITE)
button3_text = font.render("Sair", True, WHITE)
texto_instrucao = font.render('Ataque     Movimentação', True, (WHITE))

title_rect = title_text.get_rect(center=(size[0] / 2, size[1] / 4))
button1_rect = button1_text.get_rect(center=(size[0] / 2, size[1] / 2))
button2_rect = button2_text.get_rect(center=(size[0] / 2, size[1] / 2 + 50))
button3_rect = button3_text.get_rect(center=(size[0] / 2, size[1] / 2 + 100))

# criar a janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("FURIA NATURAL")

# imagens
fundo_menu = pygame.transform.scale(pygame.image.load("images/imagem_menu.png"), (largura,altura))
fundo_final = pygame.transform.scale(pygame.image.load("images/ceu.png"), (largura,altura))
fundo_jogo_fase1 = pygame.transform.scale(pygame.image.load("images/water-background.png"), (largura+50,altura+10))
fundo_jogo_fase2 = pygame.transform.scale(pygame.image.load("images/neve_fundo.png"), (largura+50,altura+10))
fundo_jogo_fase3 = pygame.transform.scale(pygame.image.load("images/fundofogo.png"), (largura+50,altura+10))
game_over_foto = pygame.transform.scale(pygame.image.load("images/Game_Over_Logo.png"), (400,300))

boneco1_1 = pygame.image.load("images/nadador5.png")
boneco1_2 = pygame.image.load("images/nadador6.png")
boneco1_3 = pygame.image.load("images/nadador7.png")
boneco1_4 = pygame.image.load("images/nadador8.png")

boneco2_1 = pygame.image.load("images/laura5.png")
boneco2_2 = pygame.image.load("images/laura6.png")
boneco2_3 = pygame.image.load("images/laura7.png")
boneco2_4 = pygame.image.load("images/laura8.png")

boneco3_1 = pygame.image.load("images/lucas5.png")
boneco3_2 = pygame.image.load("images/lucas6.png")
boneco3_3 = pygame.image.load("images/lucas7.png")
boneco3_4 = pygame.image.load("images/lucas8.png")

coin = pygame.image.load("images/coin1.png")
pedra = pygame.image.load("images/searock1.png")
pedra_azul =  pygame.transform.scale(pygame.image.load("images/pedra_azul.png"), (80, 80))
pedra_bola = pygame.image.load("images/pedrabola1.png")
arvore = pygame.transform.scale(pygame.image.load("images/arverefogo.png"), (80, 100))
volume_imagem = pygame.transform.scale(pygame.image.load("images/volume.png"), (largura_botao, altura_botao))
volume_imagem_mudo = pygame.transform.scale(pygame.image.load("images/volume_mudo.png"), (largura_botao, altura_botao))
tecla_x = pygame.transform.scale(pygame.image.load("images/tecla_x.png"), (100, 100))
teclas_setas = pygame.transform.scale(pygame.image.load("images/teclas_setas.png"), (250, 150))

fotomenu1_1 = pygame.image.load("images/nadador1.png")
fotomenu1_2 = pygame.image.load("images/nadador2.png")
fotomenu1_3 = pygame.image.load("images/nadador3.png")
fotomenu1_4 = pygame.image.load("images/nadador4.png")

fotomenu2_1 = pygame.image.load("images/laura1.png")
fotomenu2_2 = pygame.image.load("images/laura2.png")
fotomenu2_3 = pygame.image.load("images/laura3.png")
fotomenu2_4 = pygame.image.load("images/laura4.png")

fotomenu3_1 = pygame.image.load("images/lucas1.png")
fotomenu3_2 = pygame.image.load("images/lucas2.png")
fotomenu3_3 = pygame.image.load("images/lucas3.png")
fotomenu3_4 = pygame.image.load("images/lucas4.png")

# criar classe imagem
personagem = Imagem(boneco1_1, (360, 530), [5, 5])
moeda1 = Imagem(coin, (200, 20), [0, 3])
ataque = Imagem(pedra_bola, (0, 1000), [0, 5])

fotomenu1 = Imagem(fotomenu1_1, (280, 530), [0, 0])
fotomenu2 = Imagem(fotomenu2_1, (380, 530), [0, 0])
fotomenu3 = Imagem(fotomenu3_1, (480, 530), [0, 0])

obst1_1 = Imagem(pedra, (randint(0, 245),-200), [0, 6])
obst1_2 = Imagem(pedra, (randint(246, 490),-600), [0, 6])
obst1_3 = Imagem(pedra, (randint(491, 735),-400), [0, 6])

obst2_1 = Imagem(pedra_azul, (randint(0, 245),-200), [0, 6])
obst2_2 = Imagem(pedra_azul, (randint(246, 490),-600), [0, 6])
obst2_3 = Imagem(pedra_azul, (randint(491, 735),-400), [0, 6])

obst3_1 = Imagem(arvore, (randint(0, 245),-200), [0, 6])
obst3_2 = Imagem(arvore, (randint(246, 490),-600), [0, 6])
obst3_3 = Imagem(arvore, (randint(491, 735),-400), [0, 6])

fundo_1 = Imagem(fundo_jogo_fase1, (0,0), [1,6])
fundo_2 = Imagem(fundo_jogo_fase1, (0,-altura), [1,6])

imagem_tecla_x = Imagem(tecla_x, (1000,1000), [0,0])
imagem_teclas_setas = Imagem(teclas_setas, (1000,1000), [0,0])

# criar o grupo de sprites
sprites_menu = pygame.sprite.Group(fotomenu1, fotomenu2, fotomenu3, imagem_tecla_x, imagem_teclas_setas)
sprites = pygame.sprite.Group(fundo_1, fundo_2, personagem, moeda1, ataque, 
                              obst1_1, obst1_2, obst1_3,
                              obst2_1, obst2_2, obst2_3,
                              obst3_1, obst3_2, obst3_3)

# criar sons
coin_sfx = pygame.mixer.Sound("sounds/coin3.mp3")
col_per_obs = pygame.mixer.Sound("sounds/breaking-bone.mp3")
col_atk_obs = pygame.mixer.Sound("sounds/breaking-stone.mp3")

# criar area do click do botao
button_rect = pygame.Rect(740, 5, largura_botao, altura_botao)

# Para a tela de score
jogadores = ["Thaís", "João", "Ana", "Hudson", "Laura", "Gustavo", "Mariana", "Nicholas", "Luiz", "Rafael", "Larissa", "Gabriela", "Marcela"]

scores = []
for i in range(65, -1, -5):
    scores.append(i)

# criando objeto Clock
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # configurado o timer do Pygame para execução a cada 1 segundo

# ------------------------- LOOP PRINCIPAL -------------------------

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    # ---------- LOOP DO MENU ----------
    while menu_var == 1: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique do mouse ocorreu em algum botão
                if button1_rect.collidepoint(event.pos):
                    menu_var = 0
                elif button2_rect.collidepoint(event.pos):
                    instrucao_flag = 1
                    button1_rect = button1_text.get_rect(center=(size[0] / 6, size[1] / 2))
                    button2_rect = button2_text.get_rect(center=(size[0] / 6, size[1] / 2 + 50))
                    button3_rect = button3_text.get_rect(center=(size[0] / 6, size[1] / 2 + 100))
                    imagem_tecla_x.rect = (300,300)
                    imagem_teclas_setas.rect = (470,240)
                elif button3_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                
                if event.button == 1:  # Botao esquerdo do mouse
                        if button_rect.collidepoint(event.pos):
                            tocar_som = not tocar_som

        # Movimento personagens no menu
        if count_personagem_menu == 7:
            if imagem_personagem_menu == 1:
                fotomenu1.image = fotomenu1_2
                fotomenu2.image = fotomenu2_2
                fotomenu3.image = fotomenu3_2
                imagem_personagem_menu = 2
                count_personagem_menu = 0
            elif imagem_personagem_menu == 2:
                fotomenu1.image = fotomenu1_3
                fotomenu2.image = fotomenu2_3
                fotomenu3.image = fotomenu3_3
                imagem_personagem_menu = 3
                count_personagem_menu = 0
            elif imagem_personagem_menu == 3:
                fotomenu1.image = fotomenu1_4
                fotomenu2.image = fotomenu2_4
                fotomenu3.image = fotomenu3_4
                imagem_personagem_menu = 4
                count_personagem_menu = 0
            elif imagem_personagem_menu == 4:
                fotomenu1.image = fotomenu1_1
                fotomenu2.image = fotomenu2_1
                fotomenu3.image = fotomenu3_1
                imagem_personagem_menu = 1
                count_personagem_menu = 0
        count_personagem_menu += 1
        
        tela.fill(BLACK)
        tela.blit(fundo_menu, (0,0))

        sprites_menu.draw(tela)

        # plotar botão
        if tocar_som:
            tela.blit(volume_imagem, button_rect)
        else:
            tela.blit(volume_imagem_mudo, button_rect)

        tela.blit(title_text, title_rect)

        # Desenha os botões na tela
        tela.blit(button1_text, button1_rect)
        tela.blit(button2_text, button2_rect)
        tela.blit(button3_text, button3_rect)

        if instrucao_flag == 1:
            tela.blit(texto_instrucao, (290, 400))

        # Atualiza a tela
        pygame.display.flip()

        # Controle de atualização de quadros
        clock.tick(CLOCK)
    
    # ---------- LOOP DO JOGO ----------
    while fase != 4:
        #define imagens para as fases
        if fase == 1:
            temp_personagem_1 = boneco1_1
            temp_personagem_2 = boneco1_2
            temp_personagem_3 = boneco1_3
            temp_personagem_4 = boneco1_4
            fundo_1.image = fundo_jogo_fase1
            fundo_2.image = fundo_jogo_fase1
            obstaculo_1 = obst1_1
            obstaculo_2 = obst1_2
            obstaculo_3 = obst1_3
        if fase == 2:
            obst1_1.rect.x = -1000
            obst1_1.rect.y = -1000
            obst1_2.rect.x = -1000
            obst1_2.rect.y = -1000 
            obst1_3.rect.x = -1000
            obst1_3.rect.y = -1000 

            temp_personagem_1 = boneco2_1
            temp_personagem_2 = boneco2_2
            temp_personagem_3 = boneco2_3
            temp_personagem_4 = boneco2_4
            fundo_1.image = fundo_jogo_fase2
            fundo_2.image = fundo_jogo_fase2
            obstaculo_1 = obst2_1
            obstaculo_2 = obst2_2
            obstaculo_3 = obst2_3

        if fase == 3:
            obst2_1.rect.x = -1000
            obst2_1.rect.y = -1000
            obst2_2.rect.x = -1000
            obst2_2.rect.y = -1000 
            obst2_3.rect.x = -1000
            obst2_3.rect.y = -1000 

            temp_personagem_1 = boneco3_1
            temp_personagem_2 = boneco3_2
            temp_personagem_3 = boneco3_3
            temp_personagem_4 = boneco3_4
            fundo_1.image = fundo_jogo_fase3
            fundo_2.image = fundo_jogo_fase3
            obstaculo_1 = obst3_1
            obstaculo_2 = obst3_2
            obstaculo_3 = obst3_3

        # verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #capturando evendo de relogio a cada 1 segundo e atualizando a variável contadora
            if event.type == CLOCKTICK:
                temporizador = temporizador -1
            
        # finalizando o jogo
        if vidas == 0: break

        if temporizador == 0: 
            fase += 1
            temporizador = tempo
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botao esquerdo do mouse
                    if button_rect.collidepoint(event.pos):
                        tocar_som = not tocar_som

        # Verifica se alguma tecla foi pressionada, e captura o evento
        pressed = pygame.key.get_pressed()

        # Verifica qual tecla (seta) foi pressionada e atualiza o vetor Posicao de acordo com a Velocidade
        if pressed[pygame.K_LEFT]: personagem.rect.x -= personagem.velocidade[0]
        if pressed[pygame.K_RIGHT]: personagem.rect.x += personagem.velocidade[0]
        if pressed[pygame.K_UP]: personagem.rect.y -= personagem.velocidade[1]
        if pressed[pygame.K_DOWN]: personagem.rect.y += personagem.velocidade[1]

        # Nao deixar o boneco sair da tela
        if personagem.rect.x < 0: personagem.rect.x = 0
        if personagem.rect.x > largura-60: personagem.rect.x = largura-60
        if personagem.rect.y < 0: personagem.rect.y = 0
        if personagem.rect.y > altura-60: personagem.rect.y = altura-60
        
        # Movimento do personagem
        if count_personagem == 7:
            if imagem_personagem == 1:
                personagem.image = temp_personagem_2
                imagem_personagem = 2
                count_personagem = 0
            elif imagem_personagem == 2:
                personagem.image = temp_personagem_3
                imagem_personagem = 3
                count_personagem = 0
            elif imagem_personagem == 3:
                personagem.image = temp_personagem_4
                imagem_personagem = 4
                count_personagem = 0
            elif imagem_personagem == 4:
                personagem.image = temp_personagem_1
                imagem_personagem = 1
                count_personagem = 0
        count_personagem += 1

        # movimento do fundo
        # fundo 1
        fundo_1.rect.y += fundo_1.velocidade[1]
        if fundo_1.rect.y > altura: fundo_1.rect.y = -altura
        #fundo 2
        fundo_2.rect.y += fundo_2.velocidade[1]
        if fundo_2.rect.y > altura: fundo_2.rect.y = -altura

        fundo_1.rect.x += flag_fundo
        fundo_2.rect.x += flag_fundo

        # MOEDAS
        # Movimentar moeda
        moeda1.rect.y += moeda1.velocidade[1]
        if moeda1.rect.y > altura: 
            moeda1.rect.y = -100
            moeda1.rect.x = randint(0, largura-50)
        # colisão do personagem com a moeda
        if pygame.sprite.collide_rect(personagem, moeda1):
            #coin_sfx.play()
            Tocar(coin_sfx)
            pontos += 1
            moeda1.rect.y = -100
            moeda1.rect.x = randint(0, largura-50)

        # OBSTACULOS
        # Movimentar obstaculo 1
        obstaculo_1.rect.y += obstaculo_1.velocidade[1]
        if obstaculo_1.rect.y > altura: 
            obstaculo_1.rect.y = -100
            obstaculo_1.rect.x = randint(0, 245)
        # colisão do personagem com obstaculo 1
        if pygame.sprite.collide_rect(personagem, obstaculo_1):
            Tocar(col_per_obs)
            vidas -= 1
            obstaculo_1.rect.y = -100
            obstaculo_1.rect.x = randint(0, 245)

        # Movimentar obstaculo 2
        obstaculo_2.rect.y += obstaculo_2.velocidade[1]
        if obstaculo_2.rect.y > altura: 
            obstaculo_2.rect.y = -100
            obstaculo_2.rect.x = randint(246, 490)
        # colisão do personagem com obstaculo 2
        if pygame.sprite.collide_rect(personagem, obstaculo_2):
            Tocar(col_per_obs)
            vidas -= 1
            obstaculo_2.rect.y = -100
            obstaculo_2.rect.x = randint(246, 490)

        # Movimentar obstaculo 3
        obstaculo_3.rect.y += obstaculo_3.velocidade[1]
        if obstaculo_3.rect.y > altura: 
            obstaculo_3.rect.y = -100
            obstaculo_3.rect.x = randint(491, 735)
        # colisão do personagem com obstaculo 2
        if pygame.sprite.collide_rect(personagem, obstaculo_3):
            Tocar(col_per_obs)
            vidas -= 1
            obstaculo_3.rect.y = -100
            obstaculo_3.rect.x = randint(491, 735)

        # ATAQUE
        # Movimentar ataque
        if event.type == KEYUP and pode_atacar == True:
            if event.key==K_x:
                pode_atacar = False
                ataque.rect.y = personagem.rect.y
                ataque.rect.x = personagem.rect.x +15
                
        if pode_atacar == False: ataque.rect.y -= ataque.velocidade[1]
        
        if ataque.rect.y < -10: 
            ataque.rect.y = 1000
            pode_atacar = True

        # colisão com obstaculos
        # 1
        if pygame.sprite.collide_rect(ataque, obstaculo_1):
            Tocar(col_atk_obs)
            pontos += 1
            obstaculo_1.rect.y = -100
            obstaculo_1.rect.x = randint(0, 245)
            ataque.rect.y = 1000
            pode_atacar = True
        # 2
        if pygame.sprite.collide_rect(ataque, obstaculo_2):
            Tocar(col_atk_obs)
            pontos += 1
            obstaculo_2.rect.y = -100
            obstaculo_2.rect.x = randint(246, 490)
            ataque.rect.y = 1000
            pode_atacar = True
        # 3
        if pygame.sprite.collide_rect(ataque, obstaculo_3):
            Tocar(col_atk_obs)
            pontos += 1
            obstaculo_3.rect.y = -100
            obstaculo_3.rect.x = randint(491, 735)
            ataque.rect.y = 1000
            pode_atacar = True

        # desenhar as imagens na tela
        tela.fill(GREY)
        sprites.draw(tela)

        # plotar botão
        if tocar_som:
            tela.blit(volume_imagem, button_rect)
        else:
            tela.blit(volume_imagem_mudo, button_rect)

        # cronometro 
        timer1 = font.render('Tempo: ' + str(temporizador), True, (BLACK))
        tela.blit(timer1, (20, 20))

        # pontos
        score1 = font.render('Pontos: '+str(pontos), True, (GREEN))
        tela.blit(score1, (20, 60))

        # vidas
        lives = font.render('Vidas: '+str(vidas), True, (RED))
        tela.blit(lives, (20, 100))

        clock.tick(CLOCK)

        # atualizar a tela
        pygame.display.update()

    # ---------- LOOP SCORE ----------
    #pontos = pontos*10
    for i in range (len(scores)):
        if pontos >= scores[i]:
            scores.insert(i, pontos)
            jogadores.insert(i, "Você")
            break

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        tela.blit(fundo_final, (0,0))
        tela.blit(game_over_foto, (350, 150))

        desenhar_ranking()
        pygame.display.update()

    pygame.quit() 
    exit()