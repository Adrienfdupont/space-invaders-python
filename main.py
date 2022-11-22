import pygame
import os
from game import Game
from ship import Ship

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


def draw_window():
    window.blit(background, (0, 0))

    # affichage du vaisseau
    ship.draw(window)

    # affichage des missiles
    for missile in ship.missiles:
        missile.draw(window)

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
