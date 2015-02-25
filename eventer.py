from __future__ import print_function
import pygame, sys
from pygame.locals import *
from config import Config as C
import render
from render import Render as R
from game import Game as G
from debugator import debugator



class Eventer(object):

    commands = []
    
    @staticmethod
    # @debugator
    def handle():
        Eventer.commands = []
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                for inpt in C.keys_dict:
                    if eval(inpt) == event.key:
                        Eventer.commands.append(C.keys_dict[inpt])
            else:
                for inpt in C.keys_dict:
                    if eval(inpt) == event.type:
                        Eventer.commands.append(C.keys_dict[inpt])
            if Eventer.commands:
                print ('The last element of the command list:', Eventer.commands[-1] + '.')

        for command in Eventer.commands:
            if command == 'pause':
                G.switch_pause()
            elif command == 'quit':
                pygame.quit()
                sys.exit()
            elif command == 'save':
                G.save()
            elif command == 'load':
                G.load()
            elif command == 'main_menu':
                pass
            elif command == 'show_info':
                G.show_info()
            elif command == 'new_game':
                G.new_game()
            elif command == 'reload_resources':
                C.load_config()
                R.setup()
            elif command == 'switch_fullscreen':
                if C.config_dict['fullscreen'] == 1:
                    C.config_dict['fullscreen'] = 0
                else:
                    C.config_dict['fullscreen'] = 1
                R.setup()
            elif command == 'camera_left':
                render.Camera.move((10, 0))
            elif command == 'camera_right':
                render.Camera.move((-10, 0))
            elif command == 'camera_up':
                render.Camera.move((0, 10))
            elif command == 'camera_down':
                render.Camera.move((0, -10))
