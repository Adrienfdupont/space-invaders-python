import pygame
import os
from ship import Ship

# créer la fenêtre de jeu
FPS = 60
NAME = "Space Invaders"
WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME)

# récupérer l'image du background et la traiter
BG_FILE_NAME = "background.jpg"
bg_path = os.path.join("assets", "images", BG_FILE_NAME)
bg_image = pygame.image.load(bg_path).convert()
background = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# générer le vaisseau
x = WIDTH // 2
y = HEIGHT - 30
ship = Ship(x, y)


def draw_window():
    WINDOW.blit(background, (0, 0))

    # affichage du vaisseau
    ship.draw(WINDOW)

    # affichage des missiles
    for missile in ship.missiles:
        missile.draw(WINDOW)

    pygame.display.update()


def handle_input(key):
    if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
        ship.move(key, WIDTH)
    elif key[pygame.K_SPACE]:
        ship.shoot()


def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
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
