
ANSI_FG_COLOUR_CODES = {
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
# background colours are the same but value-shifted by 10
ANSI_BG_COLOUR_CODES = {key: ANSI_FG_COLOUR_CODES[key] +
    10 for key in ANSI_FG_COLOUR_CODES}
