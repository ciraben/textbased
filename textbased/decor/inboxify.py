
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
