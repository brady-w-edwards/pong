import pygame
from rectangle import *
from constants import PLAYER_RAQUET_HEIGHT, PLAYER_RAQUET_WIDTH, PLAYER_SPEED, SCREEN_HEIGHT


class PlayerRight(Rectangle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = PLAYER_RAQUET_WIDTH
        self.height = PLAYER_RAQUET_HEIGHT
        self.score = 0
        
    def rectangle(self):
        top = self.position.y - PLAYER_RAQUET_HEIGHT/2
        left = self.position.x - PLAYER_RAQUET_WIDTH/2
        width = self.width
        height = self.height
        return [left, top, width, height]

    def draw(self, screen):
        pygame.draw.rect(screen, "green", self.rectangle(), width=0)

    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * PLAYER_SPEED * dt
        
    def update(self, dt):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.move(-dt)
        if key[pygame.K_DOWN]:
            self.move(dt)
