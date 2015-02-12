#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This module is the game starter. Run it for play the game.

Pygame is initialized here. The main game objects are created (configurator, renderer, game etc.).
The main loop is here.
"""
import pygame
pygame.init()

import configurator, renderer, game, eventer

c = configurator.Configurator()

r = renderer.Renderer(c)
g = game.Game(r, c)
e = eventer.Eventer(c, g, r)


while True:
    e.handle()
    g.update()
    r.render()
