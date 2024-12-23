import pygame
from rectangle import *
from constants import NET_HEIGHT, NET_WIDTH


class Net(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def rectangle(self):
        top = self.position.y
        left = self.position.x
        width = NET_WIDTH
        height = NET_HEIGHT
        return [left, top, width, height]

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rectangle(), width=2)