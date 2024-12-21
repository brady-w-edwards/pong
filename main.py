import sys
import pygame
from constants import *
from left_player import PlayerLeft
from right_player import PlayerRight
from net import Net
from ball import Ball
from court import PongCourt

def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    dt = 0

    # CREATE GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    court = pygame.sprite.Group()

    # ASSIGN CONTAINERS
    PlayerLeft.containers = (updatable, drawable)
    PlayerRight.containers = (updatable,drawable)
    Net.containers = (updatable, drawable)
    Ball.containers = (court, updatable, drawable)
    PongCourt.containers = (updatable)

    # CREATE GAME OBJECTS
    player1 = PlayerLeft(PLAYER_START_POSITION_X, PLAYER_START_POSITION_Y)
    player2 = PlayerRight(SCREEN_WIDTH - PLAYER_START_POSITION_X, PLAYER_START_POSITION_Y)
    game_ball = Ball(SCREEN_WIDTH/2, PLAYER_START_POSITION_Y, BALL_RADIUS)
    net = Net(SCREEN_WIDTH/2, 0)
    game_court = PongCourt(SCREEN_WIDTH, SCREEN_HEIGHT)

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for ball in court:
            if ball.collision(player1.rectangle()):
                ball.paddle_rebound(player1)
            if ball.collision(player2.rectangle()):
                ball.paddle_rebound(player2)
            # if ball.collision(game_court):
            #     ball.rebound()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # re-render display
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()