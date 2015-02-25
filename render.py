from __future__ import print_function
import pygame
from config import Config as C
from config import GAME_NAME
from debugator import debugator
import os

class Render(object):
    pause_fps = 5
    used_fps = 5
    flags = 0
    image = None
    rect = None
    fpsclock = None

    image_paths = {}  # name without ext is key, full path is value
    sound_paths = {}
    sprite_container = None

    @staticmethod
    @debugator
    def setup():
        pygame.init()

        Render.pause_fps = 5
        Render.used_fps = C.config_dict['maxfps']

        if C.config_dict['fullscreen']:
            pygame.display.set_mode(C.config_dict['resolution'], pygame.FULLSCREEN)
        else:
            pygame.display.set_mode(C.config_dict['resolution'])
        pygame.display.set_caption(GAME_NAME)
        Render.image = pygame.display.get_surface()
        Render.rect = Render.image.get_rect()
        Render.fpsclock = FpsClock()


    @staticmethod
    @debugator
    def load_resources():
        Render.image_paths = Render.do_resource_paths_dict('.png')
        Render.sound_paths = Render.do_resource_paths_dict('.ogg')

        Render.sprite_container = SpriteManager()


    @staticmethod
    @debugator
    def do_resource_paths_dict(ext):
        images = {}
        for path in C.mods_paths:
            for item in os.listdir(path):
                if os.path.isfile(path + os.sep + item):
                    if item.lower().endswith(ext):
                        images.update({item.rsplit(ext,1)[0]: path+'/'+item})
                        print(path+'/'+item, 'loaded.')
                        print(item.rsplit(ext,1)[0])

        for n, p in images.items():
            print(n, '\t', p)
        return images

    @staticmethod
    @debugator
    def set_pause(bool):
        if bool:
            Render.used_fps = Render.pause_fps
        else:
            Render.used_fps = C.config_dict['maxfps']

    @staticmethod
    # @debugator
    def render():
        Render.image.fill((240,240,240))
        Render.sprite_container.update()
        Render.sprite_container.draw(Render.image)
        Render.fpsclock.update(Render.used_fps)
        Render.image.blit(Render.fpsclock.image,(0,0))
        pygame.display.flip()


class FpsClock(pygame.sprite.DirtySprite):
    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 70)
        self.color = (90,90,90)
    def update(self,fps):
        self.fps_str = str(int(self.clock.get_fps()))
        self.image = self.font.render(self.fps_str, 0, self.color)
        self.rect = self.image.get_rect()
        self.clock.tick(fps)

class SpriteManager(pygame.sprite.LayeredDirty):
    def __init__(self):
        super(SpriteManager, self).__init__()

    def register(self, pl, id):
        data = pl.give_me_data(id)
        self.add(Sprite(data['id'], data['appearance'], data['layer']))

    def update(self):
        super(SpriteManager, self).update()
        # Camera.pos = (0, 0)


class Camera(object):

    pos = [0, 0]

    @staticmethod
    @debugator
    def move(move):
        Camera.pos = [Camera.pos[0] + move[0], Camera.pos[1] + move[1]]

    @staticmethod
    @debugator
    def stop_left():
        Camera.pos[0] = 0

    @staticmethod
    @debugator
    def stop_right():
        Camera.pos[0] = 0

    @staticmethod
    @debugator
    def stop_up():
        Camera.pos[1] = 0

    @staticmethod
    @debugator
    def stop_down():
        Camera.pos[1] = 0


class Sprite(pygame.sprite.DirtySprite):
    def __init__(self, id, img, layer):
        super(Sprite, self).__init__()
        self.id = id
        self.layer = layer
        self.image = pygame.image.load(Render.image_paths[img]).convert_alpha()
        self.rect = self.image.get_rect()
        # self.rect.center = Render.rect.center

    def update(self):

        self.dirty = 1
        for group in self.groups():
            group.change_layer(self, self.layer)
        self.rect.move_ip(Camera.pos)
