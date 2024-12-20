import pygame
from rectangle import *
from constants import PLAYER_RAQUET_HEIGHT, PLAYER_RAQUET_WIDTH, PLAYER_SPEED


class PlayerLeft(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = PLAYER_RAQUET_WIDTH
        self.height = PLAYER_RAQUET_HEIGHT
        
    def rectangle(self):
        top = self.position.y + PLAYER_RAQUET_HEIGHT/2
        left = self.position.x - PLAYER_RAQUET_WIDTH/2
        width = self.width
        height = self.height
        return [left, top, width, height]

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rectangle(), width=2)

    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.move(-dt)
        if key[pygame.K_s]:
            self.move(dt)
