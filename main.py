import pygame
import os
from Ship import Ship

# créer la fenêtre de jeu
FPS = 60
NAME = "Space Invaders"
WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# récupérer l'image du background et la traiter
BG_PATH = os.path.join("assets", "images", "background.jpg")
BG_IMAGE = pygame.image.load(BG_PATH).convert()
BACKGROUND = pygame.transform.scale(BG_IMAGE, (WIDTH, HEIGHT))

# générer le vaisseau
SHIP = Ship(WIDTH // 2)

def main():
    pygame.display.set_caption(NAME)
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_window()

def draw_window():

    WINDOW.blit(BACKGROUND, (0, 0))
    pygame.display.update()

if __name__ == "__main__":
    main()