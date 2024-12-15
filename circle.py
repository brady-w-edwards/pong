import pygame
from right_player import PlayerRight
from left_player import PlayerLeft

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision(self, shape):
        if shape is CircleShape:
            r1 = self.radius
            r2 = shape.radius
            distance = self.position.distance_to(shape.position)
            if distance <= r1 + r2:
                return True
            
        elif shape is PlayerLeft or PlayerRight:
            r1 = self.radius
            rect_list = shape.rectangle()
            vertical_distance = rect_list[4]/2
            horizontal_distance = rect_list[3]/2
            distance = self.position.distance_to(shape.position)
            if distance <= r1 + horizontal_distance or distance <= r1 + vertical_distance:
                return True
        
        else: return False

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass