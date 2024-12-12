import pygame
from rectangle import *
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RAQUET_HEIGHT, PLAYER_RAQUET_WIDTH


class Player(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def rectangle(self):
        top = self.position.y + PLAYER_RAQUET_HEIGHT/2
        left = self.position.x - PLAYER_RAQUET_WIDTH/2
        width = PLAYER_RAQUET_WIDTH
        height = PLAYER_RAQUET_HEIGHT
        return [left, top, width, height]

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rectangle(), width=2)
