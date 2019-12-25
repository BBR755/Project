import pygame
import os
import sys
pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
screen.fill((50, 80, 255))
clock = pygame.time.Clock()
FPS = 50


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
    image = load_image("ship.png", -1)

    def __init__(self, group):
        super().__init__(group)
        print(11111)
        self.image = Ship.image
        self.rect = self.image.get_rect()
        self.rect.x = width//2
        self.rect.y = height//2

    def update(self, *args):
        print(4545)
        if args and key[pygame.K_DOWN] and self.rect.y + 10 <= height - 280:
            self.rect.y += 10
        if args and key[pygame.K_UP] and self.rect.y - 10 >= 0:
            self.rect.y -= 10
        if args and key[pygame.K_LEFT] and self.rect.x - 10 >= 0:
            self.rect.x -= 10
        if args and key[pygame.K_RIGHT] and self.rect.x + 10 <= width - 280:
            self.rect.x += 10

all_sprites = pygame.sprite.Group()
Player = pygame.sprite.Group()
player = Ship(Player)

start_screen()
running = True
while running:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            Player.update(event)

    screen.fill(pygame.Color(0, 0, 0))
    Player.draw(screen)
    #Player.update()
    pygame.display.flip()
    #clock.tick(1000)


terminate()
