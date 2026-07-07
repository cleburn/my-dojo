import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
width, height = screen.get_size()

# Constants
block_size = 20
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
font = pygame.font.SysFont(None, 48)

# Snake settings
snake = [(width // 2, height // 2),
         (width // 2 - block_size, height // 2),
         (width // 2 - 2 * block_size, height // 2)]
direction = 'RIGHT'

# Food placement
def random_food():
    while True:
        x = random.randint(0, (width - block_size) // block_size) * block_size
        y = random.randint(0, (height - block_size) // block_size) * block_size
        if (x, y) not in snake:
            return (x, y)

food = random_food()

clock = pygame.time.Clock()
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Calculate new head position
    if direction == 'UP':
        new_head = (snake[0][0], snake[0][1] - block_size)
    elif direction == 'DOWN':
        new_head = (snake[0][0], snake[0][1] + block_size)
    elif direction == 'LEFT':
        new_head = (snake[0][0] - block_size, snake[0][1])
    elif direction == 'RIGHT':
        new_head = (snake[0][0] + block_size, snake[0][1])

    # Collision with walls
    if (new_head[0] < 0 or new_head[0] >= width or
        new_head[1] < 0 or new_head[1] >= height):
        game_over = True
    # Collision with self
    elif new_head in snake[1:]:
        game_over = True
    else:
        # Check if food is eaten
        if new_head == food:
            snake.insert(0, new_head)
            food = random_food()
        else:
            snake.insert(0, new_head)
            snake.pop()

    # Drawing the game
    screen.fill(black)
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], block_size, block_size))
    pygame.draw.rect(screen, red, (food[0], food[1], block_size, block_size))
    pygame.display.flip()
    clock.tick(10)

# Game over screen
text = font.render('Game Over', True, white)
text_rect = text.get_rect(center=(width // 2, height // 2))
screen.blit(text, text_rect)
pygame.display.flip()
pygame.time.wait(3000)

# Clean up
pygame.quit()
sys.exit()
