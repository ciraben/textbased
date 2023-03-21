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

def fgcol(colour):
    if colour in ANSI_FG_COLOUR_CODES:
        fgcol_code = ANSI_FG_COLOUR_CODES[colour]
    else:
        # assume colour is an RGB tuple
        pass
    def decorator(fun):
        def inner(*args, **kwargs):
            sys.stdout.write(f'\033[{fgcol_code}m')
            fun(*args, **kwargs)
            sys.stdout.write('\033[0m')
        return inner
    return decorator

def bgcol(colour):
    if colour in ANSI_BG_COLOUR_CODES:
        bgcol_code = ANSI_BG_COLOUR_CODES[colour]
    else:
        # assume colour is an RGB tuple
        pass
    def decorator(fun):
        def inner(*args, **kwargs):
            sys.stdout.write(f'\033[{bgcol_code}m')
            fun(*args, **kwargs)
            sys.stdout.write('\033[0m')
        return inner
    return decorator

if __name__ == "__main__":

    # for colour in ANSI_FG_COLOUR_CODES:
    #     fgcol(colour)(print)('hello', end='')
    #     bgcol(colour)(print)('hello')
    pass
