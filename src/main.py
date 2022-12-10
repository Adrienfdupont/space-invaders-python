import pygame
import os
from ship import Ship
from invader import Invader
from wall import Wall
from missile import Missile
from entity import Entity


WIDTH, HEIGHT = 1600, 900
game = "running"

# créer la fenêtre de jeu
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# récupérer les images de fond et les traiter
bg_path = os.path.join("assets", "images", "background.jpg")
bg_image = pygame.image.load(bg_path).convert()
background = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

gameover_path = os.path.join("assets", "images", "gameover.jpg")
gameover_image = pygame.image.load(gameover_path).convert()
gameover = pygame.transform.scale(gameover_image, (WIDTH // 2, HEIGHT // 2))

win_path = os.path.join("assets", "images", "win.jpg")
win_image = pygame.image.load(win_path).convert()
win = pygame.transform.scale(win_image, (WIDTH // 2, HEIGHT // 2))

# générer le vaisseau
x = WIDTH // 2 - Ship.WIDTH // 2
y = HEIGHT - Ship.HEIGHT
ship = Ship(x, y)

# générer les invaders
for i in range(7):
    x = i * 49 * 1.5
    y = 0 
    width, height = 49, 23
    image_file_name = "invader_3.png"
    Invader(x, y, width, height, image_file_name)
for i in range(7):
    x = i * 49 * 1.5
    y = 23 * 1.5
    width, height = 49, 33
    image_file_name = "invader_2.png"
    Invader(x, y, width, height, image_file_name)
for i in range(7):
    x = i * 49 * 1.5
    y = 56 * 1.5
    width, height = 49, 36
    image_file_name = "invader_1.png"
    Invader(x, y, width, height, image_file_name)

# générer les murs
section_length = WIDTH // 9
wall_number = section_length // Wall.WIDTH
for section in range(9):
    if section % 2 == 1:
        for wall in range (wall_number):
            x = section_length * section + Wall.WIDTH * wall
            y = HEIGHT - Ship.HEIGHT - 100
            Wall(x, y)
for section in range(9):
    if section % 2 == 1:
        for wall in range (wall_number):
            if wall <= 1 or wall >= wall_number - 2:
                x = section_length * section + Wall.WIDTH * wall
                y = HEIGHT - Ship.HEIGHT - 100 + Wall.HEIGHT
                Wall(x, y)


def draw_window():
    window.blit(background, (0, 0))

    x = WIDTH // 2 - WIDTH // 4
    y = HEIGHT // 2 - HEIGHT // 4

    match game:
        case "running":
            for instance in Entity.INSTANCES:
                instance.draw(window)
        case "lose":
            window.blit(gameover, (x, y))
        case "win":
            window.blit(win, (x, y))

    pygame.display.update()


def handle_input(key):
    if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
        ship.move(key, WIDTH)
    elif key[pygame.K_SPACE]:
        ship.shoot()


def logic():
    global game
    # vérifier si partie terminée
    for ship in Ship.INSTANCES:
        if ship.alive:
            break
        game = "lose"
        return

    for invader in Invader.INSTANCES:
        if invader.alive:
            break
        game = "win"
        return
    
    # déplacement des missiles
    for missile in Ship.MISSILES:
        missile.move()
        missile.check_collision(Invader.INSTANCES)
        missile.check_collision(Wall.INSTANCES)

    for missile in Invader.MISSILES:
        missile.move()
        missile.check_collision(Wall.INSTANCES)
        missile.check_collision(Ship.INSTANCES)

    # déplacement des invaders
    for invader in Invader.INSTANCES:
        invader.move(WIDTH, HEIGHT)
        invader.check_collision(Wall.INSTANCES, ship)


def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        handle_input(pygame.key.get_pressed())
        logic()
        draw_window()


if __name__ == "__main__":
    main()
