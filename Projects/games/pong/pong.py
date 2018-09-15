"""
A simple Object Oriented game of Pong.

Helps teach a bit of OO principles. But mainly focused on:

  - Event driven systems.
  - Basic Game mechanics.
  - Dynamically objects.

The code is designed to be highly extendable.

Most variables are stored in a single place. Most game objects are
dynamic (stored in lists in this case).

As a result if you want to add more on to it, it should not be difficult to do.

Simple ideas include:

  - Having multiple balls (e.g. balls spawn more balls on each hit).
  - Having 2 vs 2 games instead of 1 vs 1.
  - Varying/randomising ball speed.
  - Varying/randomising paddle speed.

and many more. Most of these can be done with a couple lines of extra code.
"""

import random
import sys

import pygame


class Paddle(pygame.Rect):
    """
    This is our simple Paddle class.

    It is in essence a rectangle. But we also have to bind it to
    some controls (up and down keys) and give it a movement speed.
    """
    def __init__(self, velocity, up_key, down_key, *args, **kwargs):
        self.velocity = velocity
        self.up_key = up_key
        self.down_key = down_key
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_height):
        """ Move the paddle based on key presses. """
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.up_key]:
            if self.y - self.velocity > 0:
                self.y -= self.velocity

        if keys_pressed[self.down_key]:
            if self.y + self.velocity < board_height - self.height:
                self.y += self.velocity


class Ball(pygame.Rect):
    """
    Similar to the Paddle class this is essentially a basic rectangle.

    It also has velocity to determine its speed.

    It also has the `angle` variable to determine y movement.
    """
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)

    def move_ball(self):
        self.x += self.velocity
        self.y += self.angle


class Pong:
    """
    The main game class.

    This holds all our objects and runs the code which allows them to interact.

    Mostly it controls our board and feeds certain parameters about the board
    to the other components (so the objects don't run off the screen).
    """
    HEIGHT = 800
    WIDTH = 1600

    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100

    BALL_WIDTH = 10
    BALL_VELOCITY = 10
    BALL_ANGLE = 0

    COLOUR = (255, 255, 255)

    def __init__(self):
        pygame.init()  # Start the pygame instance.

        # Setup the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.central_line = pygame.Rect(self.WIDTH/2, 0, 1, self.HEIGHT)

        # Create the player objects.

        self.paddles = []
        self.balls = []
        self.paddles.append(Paddle(  # The left paddle
            self.BALL_VELOCITY,
            pygame.K_w,
            pygame.K_s,
            0,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        self.paddles.append(Paddle(  # The right paddle
            self.BALL_VELOCITY,
            pygame.K_UP,
            pygame.K_DOWN,
            self.WIDTH - self.PADDLE_WIDTH,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        self.balls.append(Ball(
            self.BALL_VELOCITY,
            self.WIDTH / 2 - self.BALL_WIDTH / 2,
            self.HEIGHT / 2 - self.BALL_WIDTH / 2,
            self.BALL_WIDTH,
            self.BALL_WIDTH
        ))

        self.clock = pygame.time.Clock()

    def check_ball_hits_wall(self):
        """
        Check if a ball hits a wall.

        If it is a side wall let it bounce.

        If it hits a goal end the game. 
        """
        for ball in self.balls:
            if ball.x > self.WIDTH or ball.x < 0:
                sys.exit(1)

            if ball.y > self.HEIGHT - self.BALL_WIDTH or ball.y < 0:
                ball.angle = -ball.angle

    def check_ball_hits_paddle(self):
        """
        Predict whether a ball will hit a paddle.
        If it does it should switch directions.
        """
        for ball in self.balls:
            for paddle in self.paddles:
                if ball.colliderect(paddle):
                    ball.velocity = -ball.velocity
                    ball.angle = random.randint(-10, 10)
                    break

    def game_loop(self):
        """
        The main game loop.

        This is where we run the actual game logic, putting everything together.
        """
        while True:
            for event in pygame.event.get():
                # Add some extra ways to exit the game.
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.check_ball_hits_paddle()
            self.check_ball_hits_wall()

            # Redraw the screen.
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, self.COLOUR, self.central_line)

            for paddle in self.paddles:
                paddle.move_paddle(self.HEIGHT)
                pygame.draw.rect(self.screen, self.COLOUR, paddle)

            # We know we're not ending the game so lets move the ball here.
            for ball in self.balls:
                ball.move_ball()
                pygame.draw.rect(self.screen, self.COLOUR, ball)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    pong = Pong()
    pong.game_loop()
