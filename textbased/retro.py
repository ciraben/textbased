#!/usr/bin/env python3
import sys
import time

# def green(fun):
#     def inner(str):
#         sys.stdout.write('\033[42m')
#         print(str)
#         sys.stdout.write('\033[0m')
#     return inner

PRINT_COLOURS = {
    "black": 30,
    "red": 31,
    "dk-red": 31,
    "lt-red": 91,
    "green": 32,
    "dk-green": 32,
    "lt-green": 92,
    "yellow": 33,
    "dk-yellow": 33,
    "lt-yellow": 93,
    "blue": 34,
    "dk-blue": 34,
    "lt-blue": 94,
    "magenta": 35,
    "dk-magenta": 35,
    "lt-magenta": 95,
    "cyan": 36,
    "dk-cyan": 36,
    "lt-cyan": 96,
    "white": 37,
    "dk-white": 37,
    "lt-white": 97
}

def print(strng = '', sep = ' ',  end = '\n', speed = 1, mod = ''):

    if mod in PRINT_COLOURS:
        modifier = str(PRINT_COLOURS[mod])
    elif isinstance(mod, int):
        modifier = str(mod)
    else:
        for c in strng:
            sys.stdout.write(c)
            # how to flush this?
            sys.stdout.flush()
            time.sleep(speed/50)
        sys.stdout.write(end)
        return
    sys.stdout.write('\033[' + modifier + 'm')
    print(strng, sep, end, speed)
    sys.stdout.write('\033[0m')




if __name__ == '__main__':
    test_string = 'Ex ut eos rerum dolor temporibus magnam voluptas ad. Ducimus assumenda suscipit temporibus. Aperiam quam vero voluptatem. Porro omnis non recusandae enim totam. Architecto fugiat autem voluptate ea quia labore.'
    for i in PRINT_COLOURS:
        print(test_string[:20], speed = .5, mod = i)
