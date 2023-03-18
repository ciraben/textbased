#!/usr/bin/env python3

import string
import sys

def printChoice(*options, pfn = None):
    if options == ():
        raise TypeError("printChoice() takes at least one argument (0 given)")

    # if pfn:
    #     def print(string = '', end = '\n'):
    #         pfn(string, end = end)

    # if some arguments are lists, treat the list elements as options
    cat_options = []
    for o in options:
        if isinstance(o, str):
            cat_options.append(o)
        else:
            try:
                # is it an iterator?
                iterator = iter(o)
            except TypeError:
                # if no
                cat_options.append(str(o))
            else:
                # if yes
                cat_options += o
    #print(cat_options)
    options = cat_options

    # make sure we have enough alphabet
    if len(options) > 26:
        raise TypeError("printChoice() takes at most 26 arguments (" +   str(len(options)) + " given)")

    # print the options along with CAPITAL letters
    # print(options)
    for i in range(len(options)):
        print(string.ascii_uppercase[i], end='')
        print(' – ' + str(options[i]))

    # here we want to get input
    # then, check if the input is a letter for one of the options
    while True:
        choice = input('Your choice? > ').upper()
        if choice in string.ascii_uppercase[:len(options)]:
            result = options[string.ascii_uppercase.index(choice)]
            print('You chose ' + choice, end='')
            print(' – ' + str(result))
            return result
        print("Try entering a letter")

if __name__ == "__main__":
    # printChoice()
    choices = ('tommo', 'diana', 0)
    printChoice(choices)
    option = printChoice('tommo', 'diana', 0)
    print('You sure chose', option)
    sys.exit()

    x = Pokemon('skarmory')
    y = Pokemon('poochyena')
    z = Pokemon('poochyena')
    a = Pokemon('poochyena')
    b = Pokemon('poochyena')
    party_list = [x, y, z, a, b]
    print("Who u wanna switch in?")
    #option = printChoice(party_list)
    option = printChoice([mon.name for mon in party_list])
