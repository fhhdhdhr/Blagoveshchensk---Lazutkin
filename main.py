import pygame, sys


mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Ping-Pong')
screen = pygame.display.set_mode((600, 300), 0, 32)
font = pygame.font.SysFont(None, 30)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:

        screen.fill((160, 82, 45))
        draw_text('Пинг-Понг', font, (255, 222, 173), screen, 250, 40)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(200, 80, 200, 50)
        button_2 = pygame.Rect(200, 140, 200, 50)
        button_3 = pygame.Rect(200, 200, 200, 50)
        if button_3.collidepoint((mx, my)):
            if click:
                game()
        if button_1.collidepoint((mx, my)):
            if click:
                options()
        if button_2.collidepoint((mx, my)):
            if click:
                resault()
        pygame.draw.rect(screen, (210, 180, 140), button_1)
        pygame.draw.rect(screen, (210, 180, 140), button_2)
        pygame.draw.rect(screen, (210, 180, 140), button_3)
        draw_text('Играть', font, (255, 255, 255), screen, 250, 95)
        draw_text('Настройки', font, (255, 255, 255), screen, 250, 215)
        draw_text('Результаты', font, (255, 255, 255), screen, 250, 155)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)

def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Настройки', font, (255, 255, 255), screen, 250, 50)
        draw_text('Смена фона', font, (255, 255, 255), screen, 100, 120)
        draw_text('Отключение звука', font, (255, 255, 255), screen, 100, 100)
        print(rect1.bottomright)
        rect1 = Rect((0, 0, 30, 30))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False



        pygame.display.update()
        mainClock.tick(60)
def resault():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Результаты последних игр', font, (255, 255, 255), screen, 250, 50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False


        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Счёт', font, (255, 255, 255), screen, 260, 50)
        draw_text('[a] : [b]', font, (255, 255, 255), screen, 250, 80)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False



        pygame.display.update()
        mainClock.tick(60)

main_menu()
