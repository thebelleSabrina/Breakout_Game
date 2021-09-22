"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)

        self.button = 0  # helps the ball will be not affected by the click every round

        self.count = 0  # counts every brick break by the ball

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        # PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
        # PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
        # PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).
        self.paddle_w = paddle_width
        self.paddle_h = paddle_height
        self.paddle = GRect(width=self.paddle_w, height=self.paddle_h)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle_offset = paddle_offset
        self.window.add(self.paddle, (self.window_width - self.paddle_w) / 2, self.window_height-self.paddle_offset)

        # Center a filled ball in the graphical window
        self.r = ball_radius
        self.ball = GOval(self.r*2, self.r*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, (self.window.width-self.ball.width)/2, (self.window.height - self.ball.height)/2)

        # Draw bricks
        self.brick_row = brick_rows
        self.brick_col = brick_cols
        self.brick_w = brick_width
        self.brick_h = brick_height
        self.space = brick_spacing
        self.bo = brick_offset

        y = self.bo - (self.brick_h + self.space)  # the first brick's location
        for i in range(self.brick_row):
            x = 0
            y += self.brick_h + self.space
            for j in range(self.brick_col):
                self.brick = GRect(width=self.brick_w, height=self.brick_h)
                self.brick.filled = True
                self.window.add(self.brick, x, y)
                x += self.brick_w + self.space

        # Default initial velocity for the ball
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Initialize our mouse listeners
        onmouseclicked(self.starts)
        onmousemoved(self.paddle_move)

    def starts(self, mouse):
        """
        :param mouse: event
        :return: button, if the game starts
        """
        self.button = 1  # if the user clicks, adds 1 to the button, game starts

    def set_start(self, new_n):
        # Setter
        self.button = new_n  # if lose one live, button will change back to 0

    def get_start(self):
        # Getter
        return self.button

    def paddle_move(self, mouse):
        self.window.add(self.paddle, (mouse.x - self.paddle.width / 2), self.window_height - self.paddle_offset)
        if self.paddle.x <= 0:  # controls the paddle not move cross the window
            self.paddle.x = 0
        if self.paddle.x + self.paddle_w >= self.window_width:
            self.paddle.x = self.window.width - self.paddle_w

    def get_dx(self):
        # Getter
        return self.__dx

    def get_dy(self):
        # Getter
        return self.__dy

    def detect_obj(self):
        upper_left = self.window.get_object_at(self.ball.x, self.ball.y)
        upper_right = self.window.get_object_at(self.ball.x+2*(self.r), self.ball.y)
        lower_left = self.window.get_object_at(self.ball.x, self.ball.y+2*(self.r))
        lower_right = self.window.get_object_at(self.ball.x+2*(self.r), self.ball.y+2*(self.r))
        if upper_left is not None:   # detects four corner of the ball to know if it touches the brick
            return upper_left
        elif upper_right is not None:
            return upper_right
        elif lower_left is not None:
            return lower_left
        elif lower_right is not None:
            return lower_right

    def remove_bricks(self, obj):
        """
        :param obj: objects touched by four corners of the ball
        :return: remove the objects
        """
        if obj is not self.paddle:
            self.window.remove(obj)
            self.count += 1

    def count_bricks(self):  # counts the number of the bricks break by the ball
        if self.count == self.brick_row * self.brick_col:
            return True
















