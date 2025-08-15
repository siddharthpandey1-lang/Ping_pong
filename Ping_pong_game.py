import pygame
import random

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Ball")

clock = pygame.time.Clock()

# Player (paddle) variables
player_width = 100
player_height = 10
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - 30
player_speed = 9

# Ball variables
ball_radius = 15
ball_x = random.randint(ball_radius, SCREEN_WIDTH - ball_radius)
ball_y = 0
ball_speed = 4

running = True
score = 0

while running:
    clock.tick(60)  # 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player with left and right keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Move the ball down
    ball_y += ball_speed

    # Check if ball hits the paddle
    if (ball_y + ball_radius >= player_y and
        player_x <= ball_x <= player_x + player_width):
        score += 1
        ball_x = random.randint(ball_radius, SCREEN_WIDTH - ball_radius)
        ball_y = 0

    # Reset ball if it goes out of the screen bottom
    if ball_y > SCREEN_HEIGHT:
        ball_x = random.randint(ball_radius, SCREEN_WIDTH - ball_radius)
        ball_y = 0
        score = 0  # Reset score on miss

    # Fill screen with black
    screen.fill((0, 0, 0))

    # Draw player (rectangle)
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_width, player_height))

    # Draw ball (circle)
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)

    # Display score
    font = pygame.font.SysFont(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()