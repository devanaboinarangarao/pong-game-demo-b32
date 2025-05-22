import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
PADDLE_SPEED = 7

# Ball settings
BALL_RADIUS = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Fonts
SCORE_FONT = pygame.font.SysFont("comicsans", 50)

# Paddle class
def draw_window(left_paddle, right_paddle, ball, left_score, right_score):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, left_paddle)
    pygame.draw.rect(WIN, WHITE, right_paddle)
    pygame.draw.ellipse(WIN, WHITE, ball)
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    WIN.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    WIN.blit(right_score_text, (WIDTH*3//4 - right_score_text.get_width()//2, 20))
    pygame.display.update()

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

def handle_ball_movement(ball, ball_vel, left_paddle, right_paddle, left_score, right_score):
    ball.x += ball_vel[0]
    ball.y += ball_vel[1]
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_vel[1] *= -1
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_vel[0] *= -1
    if ball.left <= 0:
        right_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_vel[0] = -BALL_SPEED_X if random.choice([True, False]) else BALL_SPEED_X
        ball_vel[1] = -BALL_SPEED_Y if random.choice([True, False]) else BALL_SPEED_Y
    if ball.right >= WIDTH:
        left_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_vel[0] = -BALL_SPEED_X if random.choice([True, False]) else BALL_SPEED_X
        ball_vel[1] = -BALL_SPEED_Y if random.choice([True, False]) else BALL_SPEED_Y
    return left_score, right_score

def main():
    run = True
    clock = pygame.time.Clock()
    left_paddle = pygame.Rect(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)
    ball_vel = [BALL_SPEED_X if random.choice([True, False]) else -BALL_SPEED_X,
                BALL_SPEED_Y if random.choice([True, False]) else -BALL_SPEED_Y]
    left_score = 0
    right_score = 0
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        left_score, right_score = handle_ball_movement(ball, ball_vel, left_paddle, right_paddle, left_score, right_score)
        draw_window(left_paddle, right_paddle, ball, left_score, right_score)
    pygame.quit()

if __name__ == "__main__":
    main()
