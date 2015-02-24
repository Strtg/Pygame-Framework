from __future__ import print_function
import pygame
import config
import os
from debugator import debugator

class Sprite(pygame.sprite.DirtySprite):

    @debugator
    def __init__(self, filepath, mod=config.VANILLA_DIR):
        super(Sprite, self).__init__()
        self.filepath = filepath

        self.image = pygame.image.load(self.filepath)
        self.rect = self.image.get_rect()
