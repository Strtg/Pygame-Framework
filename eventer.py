from __future__ import print_function

import pygame, sys
from pygame.locals import *

class Eventer(object):

    def __init__(self, configurator, game, renderer):
        self.c = configurator
        self.g = game
        self.r = renderer
        self.commands = []

        pass

    def handle(self):
        self.commands = []
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                for inpt in self.c.keys:
                    if eval(inpt) == event.key:
                        self.commands.append(self.c.keys[inpt])
            else:
                for inpt in self.c.keys:
                    if eval(inpt) == event.type:
                        self.commands.append(self.c.keys[inpt])
            if self.commands:
                print ('The last element of the command list:', self.commands[-1] + '.')

        for command in self.commands:
            if command == 'pause':
                self.g.switch_pause()
            elif command == 'quit':
                pygame.quit()
                sys.exit()
            elif command == 'save':
                self.g.save()
            elif command == 'load':
                self.g.load()
            elif command == 'main_menu':
                pass
            elif command == 'show_info':
                self.g.show_info()
            elif command == 'new_game':
                self.g.new_game()