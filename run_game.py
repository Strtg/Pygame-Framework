#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This module is the game starter. Run it for play the game.

Pygame is initialized here. The main game objects are created (configurator, renderer, game etc.).
The main loop is here.
"""
import pygame
pygame.init()

import configurator, renderer, game

configurator = configurator.Configurator()

renderer = renderer.Renderer((550,550), fullscreen=False)
game = game.Game(renderer)

pygame.time.wait(4000)

for i in range(1000):
    game.update()
    renderer.render()
pygame.time.wait(4000)