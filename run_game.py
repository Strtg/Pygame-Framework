#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This module is the game starter. Run it for play the game.

The program is initialized here.
The main loop is here.
"""
from __future__ import print_function
from config import Config as C
from render import Render as R
from game import Game as G
from eventer import Eventer as E
import time

C.setup()
C.load_config()
C.save_config()

R.setup()
R.load_resources()
G.new()

old_time = time.time()
lag = 0.0

while True:
    new_time = time.time()
    passed_time = new_time - old_time
    old_time = new_time
    lag += passed_time

    E.handle()

    while lag >= C.config_dict['game_logic_speed']:
        G.update()
        lag -= C.config_dict['game_logic_speed']

    R.render()
