import pygame
import const
import os

class Sprite(pygame.sprite.DirtySprite):
    def __init__(self, filepath, mod=const.VANILLA_DIR):
        super(Sprite, self).__init__()
        self.filepath = filepath

        self.image = pygame.image.load(self.filepath)
        self.rect = self.image.get_rect()
