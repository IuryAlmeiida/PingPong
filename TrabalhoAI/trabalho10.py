import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
import math

Largura_Janela = 500
Altura_Janela = 500

xDaBola = 0
yDaBola = 0
Tamanho_Bola = 20
Velocidade_Bola_X = 0.12
Velocidade_Bola_Y = 0.12

flag = 0

Y_Jogador_1 = 0
Y_Jogador_2 = 0

def xDoJogador1():
    return -Largura_Janela / 2 + larguraDosJogadores() / 2

def xDoJogador2():
    return Largura_Janela / 2 - larguraDosJogadores() / 2

def larguraDosJogadores():
    return Tamanho_Bola

def alturaDosJogadores():
    return 3 * Tamanho_Bola

def atualizar():
    global xDaBola, yDaBola, Velocidade_Bola_X, Velocidade_Bola_Y, Y_Jogador_1, Y_Jogador_2

    xDaBola = xDaBola + Velocidade_Bola_X
    yDaBola = yDaBola + Velocidade_Bola_Y
    

    if (xDaBola + Tamanho_Bola / 2 > xDoJogador2() - larguraDosJogadores() / 2
    and yDaBola - Tamanho_Bola / 2 < Y_Jogador_2 + alturaDosJogadores() / 2
    and yDaBola + Tamanho_Bola / 2 > Y_Jogador_2 - alturaDosJogadores() / 2):
        Velocidade_Bola_X = -Velocidade_Bola_X

    if (xDaBola - Tamanho_Bola / 2 < xDoJogador1() + larguraDosJogadores() / 2
    and yDaBola - Tamanho_Bola / 2 < Y_Jogador_1 + alturaDosJogadores() / 2
    and yDaBola + Tamanho_Bola / 2 > Y_Jogador_1 - alturaDosJogadores() / 2):
        Velocidade_Bola_X = -Velocidade_Bola_X

    if yDaBola + Tamanho_Bola / 2 > Altura_Janela / 2:
        Velocidade_Bola_Y = -Velocidade_Bola_Y

    if yDaBola - Tamanho_Bola / 2 < -Altura_Janela / 2:
        Velocidade_Bola_Y = -Velocidade_Bola_Y

    if xDaBola < -Largura_Janela / 2.1 or xDaBola > Largura_Janela / 2.1:
        xDaBola = 0
        yDaBola = 0
        Velocidade_Bola_Y = -Velocidade_Bola_Y
        Velocidade_Bola_X = -Velocidade_Bola_X

    keys = pygame.key.get_pressed()

    if keys[K_w]:
        Y_Jogador_1 = Y_Jogador_1 + 0.25

    if keys[K_s]:
        Y_Jogador_1 = Y_Jogador_1 - 0.25
#Esse agente é igual ao anterior, mas possui a distância de detecção da bola alterada.
    if(xDaBola > 100 and xDaBola < 101 and Y_Jogador_2 < yDaBola):
        Y_Jogador_2 = Y_Jogador_2 + abs(Y_Jogador_2-yDaBola)
    if(xDaBola > 100 and xDaBola < 101 and Y_Jogador_2 > yDaBola):
        Y_Jogador_2 = Y_Jogador_2 - abs(Y_Jogador_2-yDaBola)
       

    

def desenharRetangulo(x, y, largura, altura, r, g, b):
    glColor3f(r, g, b)

    glBegin(GL_QUADS)
    glVertex2f(-0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, -0.5 * altura + y)
    glVertex2f(0.5 * largura + x, 0.5 * altura + y)
    glVertex2f(-0.5 * largura + x, 0.5 * altura + y)
    glEnd()

def desenhar():
    glViewport(0, 0, Largura_Janela, Altura_Janela)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-Largura_Janela / 2, Largura_Janela / 2, -Altura_Janela / 2, Altura_Janela / 2, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT)

    desenharRetangulo(xDaBola, yDaBola, Tamanho_Bola, Tamanho_Bola, 1, 1, 0)
    desenharRetangulo(xDoJogador1(), Y_Jogador_1, larguraDosJogadores(), alturaDosJogadores(), 1, 0, 0)
    desenharRetangulo(xDoJogador2(), Y_Jogador_2, larguraDosJogadores(), alturaDosJogadores(), 0, 0, 1)

    pygame.display.flip()

pygame.init()
pygame.display.set_mode((Largura_Janela, Altura_Janela), DOUBLEBUF | OPENGL)

while True:
    atualizar()
    desenhar()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.event.pump()

input('Press ENTER to exit')