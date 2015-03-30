import pygame
import render
import camera
import layer
import random
import formula
import metagame
import const

how_many_on_map = 0


def foo():
    print('CLICK')

class BaseSprite(pygame.sprite.DirtySprite):
    def __init__(self, image, layer, visible=0, on_click=foo):
        super(BaseSprite, self).__init__()
        try:
            self.image = render.images[image]
        except KeyError:
            self.image = image
        self.rect = self.image.get_rect()
        self.layer = layer
        self.visible = visible
        self.dirty = 0
        self.on_click = on_click

    def show(self):
        super(BaseSprite, self).update()
        self.visible = 1
        self.dirty = 1

    def hide(self):
        super(BaseSprite, self).update()
        self.visible = 0
        self.dirty = 1


    def update(self):
        super(BaseSprite, self).update()
        # self.dirty = 0

    def on_click(self):
        self.on_click

class HUD_Sprite(BaseSprite):
    def __init__(self, image, position, layer, visible=0, on_click=foo):
        super(HUD_Sprite, self).__init__(image, layer, visible, on_click)
        self.position = position
        self.rect.topleft = self.position
        render.renderable_container.add(self)
        render.renderable_container.change_layer(self, self.layer)

    def update(self):
        global how_many_on_map
        # how_many_on_map +=1
        # self.visible = 0
        super(HUD_Sprite, self).update()
        # render.renderable_container.change_layer(self, self.layer)

class OnMapSprite(BaseSprite):
    def __init__(self, image, location, layer, visible=1, on_click=foo, offset=(0, 0)):
        super(OnMapSprite, self).__init__(image, layer, visible, on_click)
        self.location = location
        self.offset = offset
        self.start_rect = self.rect.copy()
        self.start_rect.topleft = ((self.location[0] + 0) * const.GRID_SIZE + offset[0], (self.location[1] + 0) * const.GRID_SIZE + offset[1])
        # render.renderable_container.add(self)
        # render.renderable_container.change_layer(self, self.layer)

    def update(self):
        global how_many_on_map
        # how_many_on_map +=1
        # self.visible = 0
        super(OnMapSprite, self).update()

        self.old_rect = self.rect
        self.rect = self.start_rect.move(-camera.rect.x, -camera.rect.y)
        if self.start_rect.colliderect(camera.rect):
            if self.rect != self.old_rect:
                # self.visible = 1
                self.dirty = 1


class Grid(OnMapSprite):
    def __init__(self, w, h, thicknes, color):
        self.we = w * const.GRID_SIZE + thicknes / 2
        self.h = h * const.GRID_SIZE + thicknes / 2
        self.image = pygame.Surface((self.we, self.h)).convert()
        super(Grid, self).__init__(self.image, (0, 0), layer.grid)

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        p_w = 0
        while p_w <= self.we:  # vertical lines
            pygame.draw.line(self.image, color, (p_w, 0), (p_w, self.rect.h), thicknes)
            p_w += const.GRID_SIZE
        p_h = 0
        while p_h <= self.h:  # vertical lines
            pygame.draw.line(self.image, color, (0, p_h), (self.rect.w, p_h), thicknes)
            p_h += const.GRID_SIZE
        render.renderable_container.add(self)
        render.renderable_container.change_layer(self, self.layer)
    def update(self):
        super(Grid, self).update()
        # render.renderable_container.change_layer(self, self.layer)

class MapBackground(OnMapSprite):
    def __init__(self, w, h, color):
        self.w = w * const.GRID_SIZE
        self.h = h * const.GRID_SIZE
        self.image = pygame.Surface((self.w, self.h)).convert()
        super(MapBackground, self).__init__(self.image, (0, 0), layer.cosmos)
        # self.rect = self.image.get_rect()
        self.image.fill((0, 0, 5))
        # render.renderable_container.add(self)
        # render.renderable_container.change_layer(self, self.layer)


    def update(self):
        super(MapBackground, self).update()
        # self.dirty = 1
        # render.renderable_container.change_layer(self, self.layer)



class FpsClock(HUD_Sprite):
    def __init__(self):
        super(FpsClock, self).__init__('placeholder', (0,0), layer.fps)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(render.font_paths['Teleindicadores1'], 70)
        self.color = (200,90,90)
        self.pos = render.rect.topleft
        self.show()
    def update(self):
        super(FpsClock, self).update()
        self.tick(render.used_fps)
        self.dirty = 1
    def tick(self,fps):
        self.fps_str = '{:4d}'.format(int(self.clock.get_fps()))
        self.image = self.font.render(self.fps_str, 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.clock.tick(fps)


class Location(object):
    max_x = 0
    max_y = 0

    def __init__(self, x, y, max_x, max_y):
        super(Location, self).__init__()
        self.x = x
        self.y = y
        Location.max_x = max_x
        Location.max_y = max_y
        self.planets = []
        self.spaces = []
        self.nebulas = []
        self.grids = []


    def print_info(self):
        print('My coordinate are:', self.x, self.y)

class Planet(object):
    def __init__(self, location, category, name):
        super(Planet, self).__init__()
        self.name = name
        self.location = location
        self.category = category
        png_number = random.choice(['01', '02', '03', '04', '05'])
        if category == 'earth-like':
            self.png = 'earth' + png_number + '-t-'
        elif category == 'desert':
            self.png = 'desert' + png_number + '-t-'
        elif category == 'water':
            self.png = 'water' + png_number + '-t-'
        elif category == 'ice':
            self.png = 'ice' + png_number + '-t-'
        elif category == 'paradise':
            self.png = 'paradise' + png_number + '-t-'
        elif category == 'volcano':
            self.png = 'volcano' + png_number + '-t-'

        self.sprite = OnMapSprite(self.png, self.location, layer.planets)


if __name__ == '__main__':
    print 'works'