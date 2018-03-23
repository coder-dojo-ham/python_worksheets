import random
import sys

import pygame


class Config:
    """ Lets store our configuration values in a nice simple class. """
    HEIGHT = 800
    WIDTH = 1600

    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100

    BALL_WIDTH = 10
    BALL_VELOCITY = 10
    BALL_ANGLE = 0

    COLOUR = (255, 255, 255)


pygame.init()  # Start the pygame instance.

# Set up the screen.
screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
central_line = pygame.Rect(Config.WIDTH/2, 0, 1, Config.HEIGHT)

# Create the player objects.
left_paddle = pygame.Rect(
    0, 
    Config.HEIGHT / 2 - Config.PADDLE_HEIGHT / 2, 
    Config.PADDLE_WIDTH, 
    Config.PADDLE_HEIGHT
)
right_paddle = pygame.Rect(
    Config.WIDTH - Config.PADDLE_WIDTH, 
    Config.HEIGHT / 2 - Config.PADDLE_HEIGHT / 2, 
    Config.PADDLE_WIDTH, 
    Config.PADDLE_HEIGHT
)
ball = pygame.Rect(
    Config.WIDTH / 2 - Config.BALL_WIDTH / 2, 
    Config.HEIGHT / 2 - Config.BALL_WIDTH / 2, 
    Config.BALL_WIDTH, 
    Config.BALL_WIDTH
)

clock = pygame.time.Clock()


def move_paddle(paddle, key_up, key_down, keys_pressed):
    """ Move a paddle based on key presses. """
    if keys_pressed[key_up]:
        if paddle.y - 1 > 0:
            paddle = paddle.move(0, -10)

    if keys_pressed[key_down]:
        if paddle.y + 1 < Config.HEIGHT - Config.PADDLE_HEIGHT:
            paddle = paddle.move(0, 10)

    return paddle


def check_ball_hits_paddle(ball, paddle):
    """
    Predict whether a ball will hit a paddle.
    If it does it should switch directions.
    """
    ball = ball.move(Config.BALL_VELOCITY, Config.BALL_ANGLE)
    if ball.colliderect(paddle):
        Config.BALL_VELOCITY = 0 - Config.BALL_VELOCITY
        Config.BALL_ANGLE = random.randint(-10, 10)


def check_ball_hits_wall(ball):
    """
    Check if a ball hits a wall.
    
    If it is a side wall let it bounce.
    
    If it hits a goal end the game. 
    """
    ball = ball.move(Config.BALL_VELOCITY, Config.BALL_ANGLE)

    if ball.x > Config.WIDTH or ball.x < 0:
        sys.exit(1)

    if ball.y > Config.HEIGHT - Config.BALL_WIDTH or ball.y < 0:
        Config.BALL_ANGLE = 0 - Config.BALL_ANGLE


# The main game loop.
while True:

    for event in pygame.event.get():
        # Add some extra ways to exit the game.
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE, pygame.K_DELETE):
                sys.exit(1)

    # Figure out how we're moving the paddles.
    keys_pressed = pygame.key.get_pressed()
    left_paddle = move_paddle(left_paddle, pygame.K_w, pygame.K_s, pygame.key.get_pressed())
    right_paddle = move_paddle(right_paddle, pygame.K_UP, pygame.K_DOWN, pygame.key.get_pressed())

    # Check if a paddle deflects a ball.
    check_ball_hits_paddle(ball, left_paddle)
    check_ball_hits_paddle(ball, right_paddle)

    # Check if someone loses or the ball bounces on a wall.
    check_ball_hits_wall(ball)

    # We know we're not ending the game so lets move the ball here.
    ball = ball.move(Config.BALL_VELOCITY, Config.BALL_ANGLE)

    # Redraw the screen.
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, Config.COLOUR, central_line)
    pygame.draw.rect(screen, Config.COLOUR, left_paddle)
    pygame.draw.rect(screen, Config.COLOUR, right_paddle)
    pygame.draw.rect(screen, Config.COLOUR, ball)

    pygame.display.flip()
    clock.tick(60)
