import pygame
import random
import sys
import time

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
VELOCITY = 20
MAX_BOUNCES = 3
FOOD_COUNT = 3
WIN_LENGTH = 15
FPS = 10

# Colors
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def spawn_food(snake):
    food_items = []
    positions = {tuple(part) for part in snake}
    while len(food_items) < FOOD_COUNT:
        fx = random.randint(0, (CANVAS_WIDTH - SIZE) // SIZE) * SIZE
        fy = random.randint(0, (CANVAS_HEIGHT - SIZE) // SIZE) * SIZE
        if (fx, fy) not in positions:
            food_items.append([fx, fy])
            positions.add((fx, fy))
    return food_items

def draw_text(screen, text, color, y_offset=0, size=30):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(CANVAS_WIDTH//2, CANVAS_HEIGHT//2 + y_offset))
    screen.blit(surface, rect)

def run_game(screen, clock):
    x, y = 100, 100
    dx, dy = VELOCITY, 0
    bounce_count = 0
    snake = [[x, y]]
    foods = spawn_food(snake)

    running = True
    won = False
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx, dy = -VELOCITY, 0
        elif keys[pygame.K_RIGHT]:
            dx, dy = VELOCITY, 0
        elif keys[pygame.K_UP]:
            dx, dy = 0, -VELOCITY
        elif keys[pygame.K_DOWN]:
            dx, dy = 0, VELOCITY

        # Move snake
        x += dx
        y += dy

        # Bounce check
        bounced = False
        if x < 0 or x + SIZE > CANVAS_WIDTH:
            dx = -dx
            x += dx
            bounced = True
        if y < 0 or y + SIZE > CANVAS_HEIGHT:
            dy = -dy
            y += dy
            bounced = True

        if bounced:
            bounce_count += 1

        head = [x, y]
        snake.insert(0, head)

        # Food check
        ate_food = False
        for f in foods:
            if x == f[0] and y == f[1]:
                foods.remove(f)
                ate_food = True
                break

        if not ate_food:
            snake.pop()

        if len(foods) == 0:
            foods = spawn_food(snake)

        # Draw food
        for f in foods:
            pygame.draw.rect(screen, RED, (f[0], f[1], SIZE, SIZE))

        # Draw snake
        for part in snake:
            pygame.draw.rect(screen, GREEN, (part[0], part[1], SIZE, SIZE))

        # Win check
        if len(snake) >= WIN_LENGTH:
            draw_text(screen, "Yayyy! You won the game 🎉", BLUE, size=24)
            won = True
            running = False

        # Game Over
        if bounce_count >= MAX_BOUNCES:
            draw_text(screen, "Game Over 😞", RED, size=24)
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    # Show restart message
    draw_text(screen, "Press R to restart", BLACK, y_offset=40, size=20)
    pygame.display.flip()

    # Wait for R to restart
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            waiting = False
        clock.tick(15)

def main():
    pygame.init()
    screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption("Snake Game (Pygame Version)")
    clock = pygame.time.Clock()
    print("Press R to restart or E to exit the game.")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_e:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:   
                    main()
        run_game(screen, clock)

if __name__ == "__main__":
    main()
