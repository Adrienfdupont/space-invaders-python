import pygame
import os
from ship import Ship

# créer la fenêtre de jeu
fps = 60
name = "Space Invaders"
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption(name)

# récupérer l'image du background et la traiter
bg_path = os.path.join("assets", "images", "background.jpg")
bg_image = pygame.image.load(bg_path).convert()
background = pygame.transform.scale(bg_image, (width, height))

# générer le vaisseau
x = width // 2 - Ship.width // 2
y = height - 50
ship = Ship(x, y)


def handle_movement(key):
    if key[pygame.K_LEFT] and ship.rect.x > 0:
        ship.rect.x -= 5
    elif key[pygame.K_RIGHT] and ship.rect.x + Ship.width < width:
        ship.rect.x += 5
        
        
def draw_window():
    window.blit(background, (0, 0))
    window.blit(ship.image, (ship.rect.x, ship.rect.y))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed)
        draw_window()


if __name__ == "__main__":
    main()