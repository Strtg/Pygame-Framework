#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This module is the game starter. Run it for play the game.

Pygame is initialized here. The main game objects are created (configurator, renderer, game etc.).
The main loop is here.
"""
from __future__ import print_function
from config import Config as C
from render import Render as R
from game import Game as G
from eventer import Eventer as E




C.setup()
C.load_config()
C.save_config()

R.setup()
R.load_resources()
G.new()

while True:
    E.handle()
    G.update()
    R.render()
