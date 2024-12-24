import random
import pygame
from circle import CircleShape
from constants import BALL_SPEED, PLAYER_RAQUET_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH

class Ball(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(self.random_direction(), 0)
        self.random_angle = random.uniform(20, 50)
    
    def random_direction(self):
        return BALL_SPEED * random.choice([1, -1])

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=0)

    def collision(self, shape):
        circle_rect = pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius, 
            2 * self.radius, 
            2 * self.radius
            )
        shape_rect = pygame.Rect(
            shape.position.x - shape.width/2,
            shape.position.y - shape.height/2,
            shape.width,
            shape.height
        )
        if circle_rect.colliderect(shape_rect):
            return True
        else: return False

    def edge_collision(self):
        if self.position.y - self.radius <= 50 or self.position.y + self.radius >= SCREEN_HEIGHT:
            self.velocity.y *= -1

    def paddle_rebound(self, paddle):
        self.velocity.x *= -1  # Reverse direction
        # Add speed boost
        self.velocity.x *= 1.1
        self.velocity.y *= 1.1
        # Adjust angle based on collision point
        if paddle.position.y < self.position.y:
            offset = self.velocity.y - (paddle.position.y - PLAYER_RAQUET_HEIGHT / 2)
        else: offset = self.velocity.y - (paddle.position.y + PLAYER_RAQUET_HEIGHT / 2)
        self.velocity.y += offset * 0.1

    def score_point(self, player1, player2):
        if self.position.x + self.radius <= 0:
            player1.score += 1
            self.reset(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        if self.position.x - self.radius >= SCREEN_WIDTH:
            player2.score += 1
            self.reset(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    def reset(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(self.random_direction(), 0)

    def update(self, dt):
        self.position += self.velocity * dt