import pygame
import os
import sys

pygame.init()
size = width, height = 1280, 600
screen = pygame.display.set_mode(size)
screen.fill((50, 80, 255))
clock = pygame.time.Clock()
FPS = 60
run_x = False
run_y = False
x_pos = width//2
y_pos = height//2
v_x = 0
v_y = 0
speed = 150

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Star Ship", "",
                  "Правила игры:",
                  "У игрока под контролем есть космический корабль, который управляется стрелками мыши",
                  "Цель игры:"
                  "Набраться как можно больше очков."
                  "Нажмите 'SPACE', чтобы продолжить."]

    fon = pygame.transform.scale(load_image('space.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('White'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


class Ship(pygame.sprite.Sprite):
    image = load_image("ship_3.png", -1)

    def __init__(self, player_group):
        super().__init__(player_group)
        self.image = Ship.image
        self.rect = self.image.get_rect()
        self.rect.x = width//2
        self.rect.y = height//2

    def update(self, x_1, y_1):
        self.rect = self.image.get_rect().move(x_1, y_1)


all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
ship = Ship(player_group)
start_screen()
l = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    screen.fill(pygame.Color(0, 0, 0))
    if key[pygame.K_LEFT]:
        v_x = -speed
    if key[pygame.K_RIGHT]:
        v_x = speed
    if key[pygame.K_DOWN]:
        v_y = speed
    if key[pygame.K_UP]:
        v_y = -speed
    else:
        if not key[pygame.K_LEFT]:
            if v_x == -speed:
                v_x = 0
        if not key[pygame.K_RIGHT]:
            if v_x == speed:
                v_x = 0
        if not key[pygame.K_UP]:
            if v_x == -speed:
                v_y = 0
        if not key[pygame.K_DOWN]:
            if v_x == speed:
                v_y = 0
    x_pos += v_x / FPS
    y_pos += v_y / FPS
    player_group.update(x_pos, y_pos)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
    #clock.tick(1000)

terminate()
