import os
import sys
import time

SIZE = os.get_terminal_size()
WIDTH = SIZE[0]
HEIGHT = SIZE[1]

def cursor_to(x, y):
    """Move cursor to x,y.

    Places the cursor on line y in the terminal. This counts visible lines starting at the first visible line in the terminal window. Then move the cursor onto the x'th printed character on line y (counting from 1).

    Note that if there are less than x characters on line y, the cursor is moved to the final character of line y instead.

    Args:
        x (int): Character number on which the cursor is placed after clearing the screen, counting from the first character in row y.
        y (int): Line number that the cursor is placed on, counting from the first line visible on screen.
    """
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()
    time.sleep(5)


def clear(x = 1, y = 1):
    """Clear the terminal window.

    Clears the terminal window, then fills the window with HEIGHT lines of WIDTH space characters, and finally places the cursor at line 1, character 1. Optionally place the cursor at line y, character x instead.

    Args:
        x (int): Character number on which the cursor is placed after clearing the screen.
        y (int): Line number on which the cursor is placed, counting from the first line visible on screen.
    """
    sys.stdout.write("\033[2J")
    for row in range(HEIGHT):
        sys.stdout.write(" " * WIDTH)
        if row < HEIGHT - 1:
            sys.stdout.write("\n")
    cursor_to(x, y)


if __name__ == "__main__":
    # print(WIDTH)
    # print(HEIGHT)
    # time.sleep(1)
    # # cursor_to(WIDTH/2, HEIGHT/2)
    # clear(WIDTH//2, HEIGHT//2)
