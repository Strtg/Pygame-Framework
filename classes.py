import pygame
import render

class GameSprite(pygame.sprite.DirtySprite):
    def __init__(self, image, pos, layer, hud=0, visible=1):
        super(GameSprite, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.layer = layer
        self.hud = hud
        self.visible = visible
        self.dirty = 1



class SpaceObject(object):
    def __init__(self):
        self.sprite = sprite.PlanetSprite()

class Planet(SpaceObject):

    def __init__(self, owner, category, name):
        super(Planet, self).__init__()
        self.owner = owner
        self.name = name
        self.category = category




if __name__ == '__main__':
    print 'works'