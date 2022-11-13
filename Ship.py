import pygame
from Entity import Entity
import main

class Ship(Entity):
    def __init__(self, x, y):
        SHIP_WIDTH, SHIP_HEIGHT = 56, 35
        X = WIDTH
        super().__init__(x, y, SHIP_WIDTH, SHIP_HEIGHT)
    
