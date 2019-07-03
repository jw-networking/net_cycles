#!/bin/pyhton3
#lightcycles game over lan

#~~~~~~~~~~~~~~~~
#libraries
#~~~~~~~~~~~~~~~~

import curses

#~~~~~~~~~~~~~~~~
# classes
#~~~~~~~~~~~~~~~~

class Game():
    def __init__(self):
        pass


#~~~~~~~~~~~~~~~~
# local methods
#~~~~~~~~~~~~~~~~

#setup the curses environment
def init_curses(stdscr):
    stdscr.clear()
    size=(curses.LINES-2,curses.COLS-2)
    window=stdscr.subwin(*size,1,1)
    window.nodelay(1)
    return window


#main method ran in the curses wrapper
def main(stdscr):
    window=init_curses(stdscr)

#interactive curses if ran from comandline
if __name__ == "__main__":
    curses.wrapper(main)