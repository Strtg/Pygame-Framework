#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This module is the game starter. Run it for play the game. The main loop is here.

First, the main static classes (Config, Render, MetaGame) are initialized.
Next, variables for the main loop are created.
Then the main loop is started. MetaGame.update() has its own additional loop and a timer inside the main loop.
That is because the game logic should work with limited speed. The game logic is the real game.
The Render class is just a visual effect for the real game. The game can even work without Render.render(),
only a black screen will be displayed, but the game will be working.
"""

from __future__ import print_function
import time

import config
import render
import metagame
import eventer
import title_screen
import escape_screen
import side_panel
import camera
import classes

config.setup()
config.load_config()
config.save_config()
render.setup()
render.load_resources()
render.setup_fps()
metagame.setup()



old_time = time.time()
lag = 0.0

while True:
    new_time = time.time()
    passed_time = new_time - old_time
    old_time = new_time
    lag += passed_time

    eventer.handle()

    while lag >= config.config_dict['game_logic_speed']:
        metagame.update()
        lag -= config.config_dict['game_logic_speed']

    render.render()


print(classes.how_many_on_map)