from entity import Entity

class Ship(Entity):
    width, height = 56, 35
    image_file_name = "ship.png"
    
    def __init__(self, x, y):
        super().__init__(x, y, Ship.width, Ship.height, Ship.image_file_name)
