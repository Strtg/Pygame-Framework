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
                        print ('Added', self.c.keys[inpt], 'command.')
                        print ('The last element of the command list:', self.commands[-1] + '.')
        for command in self.commands:
            if command == 'pause':
                pass
            elif command == 'quit':
                pygame.quit()
                sys.exit()