import pygame
import os
from game import Game
from ship import Ship
from invader1 import Invader1
from invader2 import Invader2
from invader3 import Invader3
from entity import Entity

# créer la fenêtre de jeu
window = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
pygame.display.set_caption(Game.NAME)

# récupérer l'image du background et la traiter
bg_path = os.path.join("assets", "images", Game.IMAGE_FILE_NAME)
bg_image = pygame.image.load(bg_path).convert()
background = pygame.transform.scale(bg_image, (Game.WIDTH, Game.HEIGHT))

# générer le vaisseau
x = Game.WIDTH // 2
y = Game.HEIGHT - 30
ship = Ship(x, y)

# générer les invaders
invaders = []
interval = Invader1.WIDTH
for i in range(8):
    invaders.append(Invader3(interval * i * 2, 0))
for i in range(8):
    invaders.append(Invader2(interval * i * 2, Invader3.HEIGHT + 10))
for i in range(8):
    invaders.append(Invader1(interval * i * 2, Invader2.HEIGHT + Invader3.HEIGHT + 20))


def draw_window():
    window.blit(background, (0, 0))

    # affichage des entités
    for instance in Entity.INSTANCES:
        instance.draw(window)

    pygame.display.update()


def handle_input(key):
    if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
        ship.move(key, Game.WIDTH)
    elif key[pygame.K_SPACE]:
        ship.shoot()


def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(Game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # récupération des inputs clavier
        handle_input(pygame.key.get_pressed())

        # déplacement des missiles
        for missile in ship.missiles:
            missile.move()
        draw_window()


if __name__ == "__main__":
    main()
