from __future__ import print_function
import pickle
import os

from const import SAVES
import config
import const
import game_state
import render
import classes
import layer
import scenarios
import pygame
import camera
import title_screen
import side_panel
import escape_screen
"""
The MetaGame class is something like a game manager.

It starts new games, saves and loads games. It can pause the game.
It should do things that can be done outside the game.
To do: MetaGame should have container for commands inputed by player.
"""

is_pause = False
commands = []
difficulty_for_new_game = 'normal'
name_for_new_game = 'Unnamed Game'
is_grid = 0
grid = None
view_is_moving_left = 0
view_is_moving_up = 0
stage = 'title_screen'
# stage = 'game'
# stage = 'escape_screen'


def new():
    global grid
    game_state.setup(name_for_new_game, difficulty_for_new_game, scenarios.scenarios[0])  # object manager and game instance to save/load


    print ('NEW GAME!!!')
    # print ('BG', map_bg.rect, map_bg.location)
    side_panel.setup(scenarios.scenarios[0])
    side_panel.show()
    camera.setup()

def save():
    pass
    # f = open(SAVES + os.sep + 'savedgame' + const.SAVE_EXT, 'wb')
    # pickler = pickle.Pickler(f, 2)
    # pickler.dump(current_game_state)
    # f.close()
    # del pickler


def load():
    pass
    # global current_game_state
    # f = open(SAVES + os.sep + 'savedgame' + const.SAVE_EXT, 'rb')
    # unpickler = pickle.Unpickler(f)
    # current_game_state = unpickler.load()
    # f.close()
    # del unpickler

def setup():
    print('metagame setup')
    escape_screen.setup()
    title_screen.setup()

    if stage == 'title_screen':
        title_screen.show()
    elif stage == 'game':
        game_state.show()
    elif stage == 'escape_screen':
        escape_screen.show()

def update():
    if stage == 'title_screen':
        title_screen.update()
    elif stage == 'game':
        game_state.update()
    elif stage == 'escape_screen':
        escape_screen.update()

def mouse_down(pos):
    print('METAGAME MOUSE DOWN')
    if stage == 'title_screen':
        title_screen.mouse_click(pos)
    elif stage == 'game':
        game_state.mouse_click(pos)
    elif stage == 'escape_screen':
        escape_screen.mouse_click(pos)

def show_info():
    # print (game_state.name)
    # print (game_state.difficulty)
    # print (game_state.date_of_creating)
    print(len(render.renderable_container.sprites()))


def switch_grid():
    print(config.config_dict['grid'])
    for location in game_state.locations.values():
        print(location)
        for grid in location.grids:
            if config.config_dict['grid']:
                grid.add(render.renderable_container)
                render.renderable_container.change_layer(grid, grid.layer)
            else:
                grid.kill()

def switch_pause():
    global is_pause
    if is_pause:
        is_pause = False
        render.set_pause(False)
    else:
        is_pause = True
        render.set_pause(True)