#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import configurator, renderer
pygame.init()

key_config = configurator.Configurator('keyboard')
options = configurator.Configurator('options')



### test shit
print key_config

renderer = renderer.Renderer((550,550), fullscreen=False)
renderer.render()
pygame.time.wait(4000)