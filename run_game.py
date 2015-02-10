#! /usr/bin/env python2
# -*- coding: utf-8 -*-

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