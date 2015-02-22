#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This module is the game starter. Run it for play the game.

Pygame is initialized here. The main game objects are created (configurator, renderer, game etc.).
The main loop is here.
"""
import pygame
pygame.init()
from config import Config as C
from render import Render as R


# import configurator, renderer, game, eventer, game_object


C.setup()
C.load_config()
C.save_config()

R.setup()
R.load_resources()

# r = renderer.Renderer(c)
# g = game.Game(r, c)
# g.name = 'crap game'
# g.difficulty = 'really crap game!!!'




# e = eventer.Eventer(c, g, r)
#
#
# while True:
#     e.handle()
#     g.update()
#     r.render()
