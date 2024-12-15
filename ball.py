import random
import pygame
from circle import CircleShape
from constants import BALL_RADIUS

class Ball(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.random_angle = random.uniform(20, 50)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def rotate(self, multiplier):
        self.rotation += self.random_angle * multiplier

    def update(self, dt):
        self.position += self.velocity * dt