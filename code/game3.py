import pygame
import os
import random
import pickle

pygame.init()

LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

velocidade_personagem = 10
velocidade_fundo = 2


def carregar_personagem():
    caminho = ("playeridle.png")
    personagem = pygame.image.load(caminho)
    return personagem


def pegar_frame_personagem(sprite_sheet, numero_frame, largura_sprite, altura_sprite):
    return sprite_sheet.subsurface(pygame.Rect(0, numero_frame * altura_sprite, largura_sprite, altura_sprite))


def desenhar_personagem(x, y, frame_atual, tamanho_personagem):
    largura_sprite = 16
    altura_sprite = 24

    personagem = carregar_personagem()
    frame = pegar_frame_personagem(personagem, frame_atual, largura_sprite, altura_sprite)

    frame_redimensionado = pygame.transform.scale(frame,
                                                  (largura_sprite * tamanho_personagem,
                                                   altura_sprite * tamanho_personagem))

    tela.blit(frame_redimensionado, (x, y))


def carregar_coletaveis():
    coletaveis = []
    coletaveis_folder = "coletaveis"
    for img_name in os.listdir(coletaveis_folder):
        if img_name.endswith(".png"):
            img_path = os.path.join(coletaveis_folder, img_name)
            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (30, 30))
            coletaveis.append(img)
    return coletaveis


def desenhar_coletavel(coletavel, posicao_coletavel):
    tela.blit(coletavel, posicao_coletavel)



def verificar_colisao(personagem_rect, coletavel_pos):
    if personagem_rect.colliderect(pygame.Rect(coletavel_pos[0], coletavel_pos[1], 30, 30)):
        return True
    return False


def carregar_fundo():
    fundo = pygame.image.load("background.png")
    fundo = pygame.transform.scale(fundo, (LARGURA_TELA * 2, ALTURA_TELA))
    return fundo



def desenhar_fundo(fundo, deslocamento):
    tela.blit(fundo, (deslocamento, 0))
    tela.blit(fundo, (deslocamento - LARGURA_TELA, 0))



def verificar_colisao_borda(x, y, largura_personagem, altura_personagem):
    if x < 0 or x + largura_personagem > LARGURA_TELA or y < 0 or y + altura_personagem > ALTURA_TELA:
        return True
    return False


def mostrar_game_over():

    fonte_game_over = pygame.font.Font("fonte2d.ttf", 74)
    texto_game_over = fonte_game_over.render("Game Over", True, VERMELHO)
    tela.blit(texto_game_over, (LARGURA_TELA // 2 - texto_game_over.get_width() // 2, ALTURA_TELA // 2 - texto_game_over.get_height() // 2))


def carregar_record():
    try:
        with open("record.pickle", "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return 0


def salvar_record(record):
    with open("record.pickle", "wb") as arquivo:
        pickle.dump(record, arquivo)


# Função principal do jogo
def jogo():
    x = LARGURA_TELA // 2
    y = ALTURA_TELA - 100
    mov_x = 0
    mov_y = 0
    coletados = 0
    coletaveis = carregar_coletaveis()


    coletavel_atual = random.choice(coletaveis)
    coletavel_pos = (random.randint(50, LARGURA_TELA - 50), random.randint(50, ALTURA_TELA - 50))

    frame_atual = 0
    animacao_speed = 10
    contador_frames = 0

    fundo = carregar_fundo()
    deslocamento_fundo = 0

    tamanho_personagem = 2

    record = carregar_record()

    rodando = True
    while rodando:
        # Loop para reiniciar o jogo após o Game Over
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    break

            if not rodando:
                break

            # Movimentação do personagem
            teclas = pygame.key.get_pressed()

            if teclas[pygame.K_LEFT]:
                mov_x = -velocidade_personagem
            elif teclas[pygame.K_RIGHT]:
                mov_x = velocidade_personagem
            else:
                mov_x = 0

            if teclas[pygame.K_UP]:
                mov_y = -velocidade_personagem
            elif teclas[pygame.K_DOWN]:
                mov_y = velocidade_personagem
            else:
                mov_y = 0

            # Atualizar a posição do personagem
            x += mov_x
            y += mov_y

            if verificar_colisao_borda(x, y, 16 * tamanho_personagem, 24 * tamanho_personagem):
                print("Você colidiu com a borda! Game Over.")
                tela.fill(PRETO)
                mostrar_game_over()

                if coletados > record:
                    record = coletados
                    salvar_record(record)

                fonte_record = pygame.font.Font(None, 36)
                texto_record = fonte_record.render(f"Buchin mais cheio: {record}", True,
                                                   BRANCO)
                tela.blit(texto_record, (LARGURA_TELA - texto_record.get_width() - 10, 10))

                pygame.display.update()
                pygame.time.delay(2000)  # Espera 2 segundos

                # Reiniciar o jogo
                x = LARGURA_TELA // 2
                y = ALTURA_TELA - 100
                coletados = 0
                tamanho_personagem = 2
                coletavel_atual = random.choice(coletaveis)
                coletavel_pos = (random.randint(50, LARGURA_TELA - 50), random.randint(50, ALTURA_TELA - 50))
                break

            tela.fill(BRANCO)

            # Desenhar o fundo em movimento
            deslocamento_fundo -= velocidade_fundo
            if deslocamento_fundo <= -LARGURA_TELA:
                deslocamento_fundo = 0

            desenhar_fundo(fundo, deslocamento_fundo)

            desenhar_personagem(x, y, frame_atual, tamanho_personagem)

            desenhar_coletavel(coletavel_atual, coletavel_pos)

            personagem_rect = pygame.Rect(x, y, 16 * tamanho_personagem, 24 * tamanho_personagem)

            if verificar_colisao(personagem_rect, coletavel_pos):
                coletados += 1
                if coletados % 3 == 0:
                    tamanho_personagem += 1

                coletavel_atual = random.choice(coletaveis)
                coletavel_pos = (random.randint(50, LARGURA_TELA - 50), random.randint(50, ALTURA_TELA - 50))

            def desenhar_contador(coletados):
                fonte_tamanho = 30
                fonte = pygame.font.Font("lovedays.ttf", fonte_tamanho)
                texto = fonte.render(f"Bucho: {coletados}", True, PRETO)

                fundo_contador = pygame.image.load(
                    "caixa.png")
                fundo_contador = pygame.transform.scale(fundo_contador, (
                texto.get_width() + 50, texto.get_height() + 10))

                tela.blit(fundo_contador, (10, 10))

                x_texto = 10 + (fundo_contador.get_width() - texto.get_width()) // 2
                y_texto = 10 + (fundo_contador.get_height() - texto.get_height()) // 2

                tela.blit(texto, (x_texto, y_texto))

            desenhar_contador(coletados)

            fonte_record = pygame.font.Font(None, 36)
            texto_record = fonte_record.render(f"Buchin mais cheio: {record}", True, BRANCO)
            tela.blit(texto_record, (LARGURA_TELA - texto_record.get_width() - 10, 10))

            contador_frames += 1
            if contador_frames >= animacao_speed:
                frame_atual = (frame_atual + 1) % 6
                contador_frames = 0

            pygame.display.update()

            pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    jogo()