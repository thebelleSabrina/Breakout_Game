"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!
    x = graphics.get_dx()
    y = graphics.get_dy()
    blood = 0
    while True:
        if blood < NUM_LIVES:
            if graphics.get_start() == 1:
                obj = graphics.detect_obj()
                if obj is not None:
                    y *= -1
                    graphics.remove_bricks(obj)
                # Check
                graphics.ball.move(x, y)
                # Update
                if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                    x *= -1
                if graphics.ball.y <= 0 or graphics.ball.y+graphics.ball.height >= graphics.window.height:
                    y *= -1
                if graphics.ball.y + graphics.ball.height >= graphics.window.height: # if the ball jumps over the window
                    blood += 1
                    graphics.set_start(0)
                    graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
                    graphics.ball.y = (graphics.window.height - graphics.ball.height) / 2
            # Pause
            pause(FRAME_RATE)
            if graphics.count_bricks():
                break
        else:
            break


if __name__ == '__main__':
    main()
