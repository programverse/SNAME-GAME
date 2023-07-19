import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the snake initial position and properties
snake_size = 20
snake_x = width // 2
snake_y = height // 2
snake_dx = 0
snake_dy = 0

# Set up the food initial position and properties
food_size = 20
food_x = random.randint(0, width - food_size) // 20 * 20
food_y = random.randint(0, height - food_size) // 20 * 20

# Set up the clock
clock = pygame.time.Clock()

# Set up the game over flag
game_over = False

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -snake_size
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = snake_size
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dy = -snake_size
                snake_dx = 0
            elif event.key == pygame.K_DOWN:
                snake_dy = snake_size
                snake_dx = 0

    # Update snake position
    snake_x += snake_dx
    snake_y += snake_dy

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, width - food_size) // 20 * 20
        food_y = random.randint(0, height - food_size) // 20 * 20

    # Clear the screen
    window.fill(BLACK)

    # Draw the snake and food
    pygame.draw.rect(window, GREEN, (snake_x, snake_y, snake_size, snake_size))
    pygame.draw.rect(window, RED, (food_x, food_y, food_size, food_size))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(10)

# Quit the game
pygame.quit()


