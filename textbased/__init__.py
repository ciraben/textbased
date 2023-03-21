# add import lines like so - one for each module
# makes import more intuitive for end-user
# allows them to access modules afterwards, like:
#   import textbased
#   x = textbased.foo.func()
import textbased.foo as foo
import textbased.decor as decor
import textbased.game as game
import textbased.retro as retro
import textbased.screen as screen
from textbased.constants import *
