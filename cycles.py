#!/bin/python3
#lightcycles game over lan

#~~~~~~~~~~~~~~~~
#libraries
#~~~~~~~~~~~~~~~~

import curses

#~~~~~~~~~~~~~~~~
# static global variables
#~~~~~~~~~~~~~~~~

borders=('|','|','-','-','/','\\','\\','/')

#~~~~~~~~~~~~~~~~
# classes
#~~~~~~~~~~~~~~~~

class Player():
    def __init__(self,name):
        self.name=name

class Net_Player(Player):
    def __init__(self):
        name="net"
        super().__init__(name)



class Board():
    def __init__(self):
        pass

class Game():
    def __init__(self):
        pass


#~~~~~~~~~~~~~~~~
# methods
#~~~~~~~~~~~~~~~~

#setup the curses environment
def init_curses(stdscr):
    stdscr.clear()
    size=(80,80)
    window=stdscr.subwin(*size,1,1)
    return window

def draw_Window(window,game):
    window.erase()
    window.border(*borders)

    window.refresh()

#main method ran in the curses wrapper
def main(stdscr):
    window=init_curses(stdscr)
    window.refresh()

#interactive curses if ran from comandline
if __name__ == "__main__":
    curses.wrapper(main)