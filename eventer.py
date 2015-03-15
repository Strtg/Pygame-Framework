from __future__ import print_function
import pygame
import sys
from pygame.locals import *

import config
import render
import metagame


class Eventer(object):

    commands = []
    
    @staticmethod
    def handle():
        Eventer.commands = []
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                for inpt in C.keys_down_dict:
                    if eval(inpt) == event.key:
                        Eventer.commands.append(C.keys_down_dict[inpt])
            elif event.type == KEYUP:
                for inpt in C.keys_up_dict:
                    if eval(inpt) == event.key:
                        Eventer.commands.append(C.keys_up_dict[inpt])

            else:
                for inpt in C.keys_down_dict:
                    if eval(inpt) == event.type:
                        Eventer.commands.append(C.keys_down_dict[inpt])
            if Eventer.commands:
                print ('The last element of the command list:', Eventer.commands[-1] + '.')

        for command in Eventer.commands:
            if command == 'pause':
                MetaGame.switch_pause()
            elif command == 'quit':
                pygame.quit()
                sys.exit()
            elif command == 'save':
                MetaGame.save()
            elif command == 'load':
                MetaGame.load()
            elif command == 'main_menu':
                pass
            elif command == 'show_info':
                MetaGame.show_info()
            elif command == 'new_game':
                MetaGame.new_game()
            elif command == 'reload_resources':
                C.load_config()
                render.Render.setup()
            elif command == 'switch_fullscreen':
                if C.config_dict['fullscreen'] == 1:
                    C.config_dict['fullscreen'] = 0
                else:
                    C.config_dict['fullscreen'] = 1
                R.setup()
            elif command == 'view_left':
                MetaGame.game.view_is_moving_left = 1
            elif command == 'view_right':
                MetaGame.game.view_is_moving_right = 1
            elif command == 'view_up':
                MetaGame.game.view_is_moving_up = 1
            elif command == 'view_down':
                MetaGame.game.view_is_moving_down = 1
            elif command == 'view_stop_left':
                MetaGame.game.view_is_moving_left = 0
            elif command == 'view_stop_right':
                MetaGame.game.view_is_moving_right = 0
            elif command == 'view_stop_up':
                MetaGame.game.view_is_moving_up = 0
            elif command == 'view_stop_down':
                MetaGame.game.view_is_moving_down = 0

