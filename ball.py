import random
import pygame
from circle import CircleShape
from constants import BALL_RADIUS, BALL_SPEED
from left_player import PlayerLeft
from right_player import PlayerRight

class Ball(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(self.random_direction(), 0)
        self.rotation = 0
        self.random_angle = random.uniform(20, 50)
    
    def random_direction(self):
        return BALL_SPEED * random.choice([1, -1])

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def rotate(self, multiplier):
        self.rotation += self.random_angle * multiplier

    def collision(self, shape):
        r1 = self.radius
        vertical_distance = shape.height/2
        horizontal_distance = shape.width/2
        distance = self.position.distance_to(shape.position)
        if distance <= r1 + horizontal_distance or distance <= r1 + vertical_distance:
            return True
    
        else: return False

    def rebound(self):
        return self.velocity * 2

    def update(self, dt):
        self.position += self.velocity * dt