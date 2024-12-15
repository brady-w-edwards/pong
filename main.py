import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from left_player import PlayerLeft
from right_player import PlayerRight
from net import Net
from ball import Ball

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # CREATE GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    ball = pygame.sprite.Group()
    court = pygame.sprite.Group()

    PlayerLeft.containers = (updatable, drawable)
    PlayerRight.containers = (updatable,drawable)
    Net.containers = (updatable, drawable)
    Ball.containers = (ball, updatable, drawable)

    player1 = PlayerLeft(SCREEN_WIDTH/16, SCREEN_HEIGHT/2)
    player2 = PlayerRight(SCREEN_WIDTH - SCREEN_WIDTH/16, SCREEN_HEIGHT - SCREEN_HEIGHT/2)
    net = Net(SCREEN_WIDTH/2, 0)

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # re-render display
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()