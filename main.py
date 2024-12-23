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
    font = pygame.font.Font(None, 24)
    pygame.display.set_caption("PONG")

    # CREATE GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    court = pygame.sprite.Group()
    players = pygame.sprite.Group()

    # ASSIGN CONTAINERS
    PlayerLeft.containers = (players, updatable, drawable)
    PlayerRight.containers = (players, updatable,drawable)
    Net.containers = (updatable, drawable)
    Ball.containers = (court, updatable, drawable)
    PongCourt.containers = (updatable)

    # CREATE GAME OBJECTS
    player1 = PlayerLeft(PLAYER_START_POSITION_X, PLAYER_START_POSITION_Y)
    player2 = PlayerRight(SCREEN_WIDTH - PLAYER_START_POSITION_X, PLAYER_START_POSITION_Y)
    game_ball = Ball(SCREEN_WIDTH/2, PLAYER_START_POSITION_Y, BALL_RADIUS)
    net = Net(SCREEN_WIDTH/2, 0)
    game_court = PongCourt(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # GAME STATES
    START_SCREEN = "start"
    PLAYING = "playing"
    game_state = START_SCREEN
    running = True

    # START SCREEN
    def draw_start_screen():
        screen.fill("black")
        title = "WELCOME, Press Enter to Begin"
        text = font.render(title, True, "white")
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

    # GAME LOOP
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if game_state == START_SCREEN and event.key == pygame.K_RETURN:
                    game_state = PLAYING

        if game_state == START_SCREEN:
            draw_start_screen()
        else:
            player1_text = font.render(f"Player 1: {player1.score}", True, "white")
            player2_text = font.render(f"Player 2: {player2.score}", True, "white")
            screen.blit(player1_text, (20,20))
            screen.blit(player2_text, (SCREEN_WIDTH/2, 20))

            for obj in updatable:
                obj.update(dt)

            for ball in court:
                if ball.collision(player1):
                    ball.paddle_rebound(player1)
                if ball.collision(player2):
                    ball.paddle_rebound(player2)
                ball.edge_collision(game_court, player1, player2)

            screen.fill("black")

            for obj in drawable:
                obj.draw(screen)

            # re-render display
            pygame.display.flip()

            # limit the framerate to 60 FPS
            dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()