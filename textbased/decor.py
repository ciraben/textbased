import sys
if __name__ == "__main__":
    from constants import ANSI_FG_COLOUR_CODES, ANSI_BG_COLOUR_CODES
else:
    from .constants import ANSI_FG_COLOUR_CODES, ANSI_BG_COLOUR_CODES

def inboxify(mystring):
    """
    Add an ASCII box around a string
    """
    lines = mystring.split('\n')
    max_length = 0
    for line in lines:
        max_length = max(len(line), max_length)
    box_line = '+' + '-' * (max_length + 2) + '+'
    new_lines = [box_line]
    for line in lines:
        new_line = line + ' ' * (max_length - len(line))
        new_line = '| ' + new_line + ' |'
        new_lines.append(new_line)
    new_lines.append(box_line)
    return '\n'.join(new_lines)

# def get_ansi_code(colour, bg = False):
#     if bg:
#         return f"38;2;{colour[0]};{colour[1]};{colour[2]}"

def fgcol(colour):
    if colour in ANSI_FG_COLOUR_CODES:
        fgcode = ANSI_FG_COLOUR_CODES[colour]
    else:
        # assume colour is an RGB tuple
        fgcode = f"38;2;{colour[0]};{colour[1]};{colour[2]}"
    def decorator(fun):
        def inner(*args, **kwargs):
            sys.stdout.write('\033[' +
                fgcode + 'm')
            fun(*args, **kwargs)
            sys.stdout.write('\033[0m')
        return inner
    return decorator

def bgcol(colour):
    if colour in ANSI_BG_COLOUR_CODES:
        bgcode = ANSI_BG_COLOUR_CODES[colour]
    else:
        # assume colour is an RGB tuple
        bgcode = f"48;2;{colour[0]};{colour[1]};{colour[2]}"
    def decorator(fun):
        def inner(*args, **kwargs):
            sys.stdout.write(f'\033[{bgcode}m')
            fun(*args, **kwargs)
            sys.stdout.write('\033[0m')
        return inner
    return decorator

if __name__ == "__main__":

    # for number in range(0, 256):
    #     for other_number in range(0, 256):
    #         bgcol((number, other_number, 255))(print)(' ', end='')
    #     print()
    # bgcol(colour)(print)('hello')
    pass
