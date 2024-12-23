import random
import pygame
from circle import CircleShape
from constants import BALL_SPEED, PLAYER_RAQUET_HEIGHT

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
        circle_rect = pygame.Rect(
            self.position.x - self.radius,
            self.position.y - self.radius, 
            2 * self.radius, 
            2 * self.radius)
        shape_rect = pygame.Rect(
            shape.position.x - shape.width/2,
            shape.position.y - shape.height/2,
            shape.width,
            shape.height
        )
        if circle_rect.colliderect(shape_rect):
            return True
        else: return False

    def edge_collision(self, court, player1, player2):
        # Create a temporary Rect object representing the court boundary
        court_rect = pygame.Rect(
            court.position.x - court.width/2,
            court.position.y - court.height/2,
            court.width,
            court.height
        )
        if self.position.y - self.radius <= court_rect.top or self.position.y + self.radius >= court_rect.bottom:
            self.velocity.y = -self.velocity.y 
        if self.position.x - self.radius <= court_rect.left:
            player1.score += 1
        if self.position.x + self.radius >= court_rect.right:
            player2.score += 1

    def paddle_rebound(self, paddle):
        self.velocity.x *= -1  # Reverse direction
        # Add speed boost
        self.velocity.x *= 1.1
        self.velocity.y *= 1.1
        # Adjust angle based on collision point
        offset = self.velocity.y - (paddle.position.y + PLAYER_RAQUET_HEIGHT / 2)
        self.velocity.y += offset * 0.1

    def update(self, dt):
        self.position += self.velocity * dt