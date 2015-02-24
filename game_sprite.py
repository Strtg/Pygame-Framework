import pygame
import config
import os

class Sprite(pygame.sprite.DirtySprite):
    def __init__(self, filepath, mod=config.VANILLA_DIR):
        super(Sprite, self).__init__()
        self.filepath = filepath

        self.image = pygame.image.load(self.filepath)
        self.rect = self.image.get_rect()
