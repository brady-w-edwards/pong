import pygame
from constants import *
from rectangle import Rectangle


class PongCourt(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

    def court_size(self):
        top = self.position.y - SCREEN_HEIGHT/2
        left = self.position.x - SCREEN_WIDTH/2
        width = self.width
        height = self.height
        return pygame.Rect(top, left, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.court_size(), width=2)

    def update(self, dt):
        self.position += self.velocity * dt