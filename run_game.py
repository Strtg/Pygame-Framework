#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This module is the game starter. Run it for play the game.

Pygame is initialized here. The main game objects are created (configurator, renderer, game etc.).
The main loop is here.
"""
import pygame
pygame.init()
import config
# import configurator, renderer, game, eventer, game_object


config.setup()

listaa = config.do_list_from_file(config.MODS_FILE)
print listaa


c = configurator.Configurator()

r = renderer.Renderer(c)
g = game.Game(r, c)
g.name = 'crap game'
g.difficulty = 'really crap game!!!'




e = eventer.Eventer(c, g, r)


while True:
    e.handle()
    g.update()
    r.render()
