from __future__ import print_function
import pygame
import sys
from pygame.locals import *

import config
import render
import metagame
import camera
import game_state


def handle():
    # global commands
    key_commands = []
    mouse_commands = []
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            for inpt in config.keys_down_dict:
                if eval(inpt) == event.key:
                    key_commands.append(config.keys_down_dict[inpt])
        elif event.type == KEYUP:
            for inpt in config.keys_up_dict:
                if eval(inpt) == event.key:
                    key_commands.append(config.keys_up_dict[inpt])
        elif event.type == MOUSEBUTTONDOWN:
            mouse_commands.append(event)

        else:
            for inpt in config.keys_down_dict:
                if eval(inpt) == event.type:
                    key_commands.append(config.keys_down_dict[inpt])
        # if key_commands:
            # print ('The last KEY command:', key_commands[-1], '.')
        if mouse_commands:
            print ('The last MOUSE command:', mouse_commands[-1], '.')

    for command in key_commands:
        if command == 'pause':
            metagame.switch_pause()
        elif command == 'grid':
            if config.config_dict['grid'] == 1:
                config.config_dict['grid'] = 0
            else:
                config.config_dict['grid'] = 1
            metagame.switch_grid()
        elif command == 'quit':
            pygame.quit()
            sys.exit()
        elif command == 'save':
            metagame.save()
        elif command == 'load':
            metagame.load()
        elif command == 'main_menu':
            pass
        elif command == 'show_info':
            metagame.show_info()
        elif command == 'new_game':
            metagame.new_game()
        elif command == 'nebulize':
            game_state.nebulize()
        elif command == 'reload_resources':
            config.load_config()
            render.Render.setup()
        elif command == 'switch_fullscreen':
            if config.config_dict['fullscreen'] == 1:
                config.config_dict['fullscreen'] = 0
            else:
                config.config_dict['fullscreen'] = 1
            render.reconfigure()
        elif command == 'view_left':
            camera.is_moving_left = 1
        elif command == 'view_right':
            camera.is_moving_right = 1
        elif command == 'view_up':
            camera.is_moving_up = 1
        elif command == 'view_down':
            camera.is_moving_down = 1
        elif command == 'view_stop_left':
            camera.is_moving_left = 0
        elif command == 'view_stop_right':
            camera.is_moving_right = 0
        elif command == 'view_stop_up':
            camera.is_moving_up = 0
        elif command == 'view_stop_down':
            camera.is_moving_down = 0

    for command in mouse_commands:
        if command.type == MOUSEBUTTONDOWN:
            metagame.mouse_down(command.pos)
