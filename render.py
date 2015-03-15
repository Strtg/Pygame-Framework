from __future__ import print_function
import pygame
import os

import config  # for configurations (resolutions, fullscreen and mod paths for image load
import const  # for game name in window caption

pause_fps = 0  # fps when pause
used_fps = 0  # current fps
screen = None  # display screen surface
rect = None  # display screen surface rect
fpsclock = None  # fps displayer and counter
image_paths = {}  # name without ext is key, full path is value
sound_paths = {}  # same as image_paths but for sound
images = {}  # loaded images
sprite_container = None  # group for all sprites


def setup():  # initialize all global variables
    pygame.init()
    global pause_fps, used_fps, screen, image_paths, rect, fpsclock, sprite_container
    pause_fps = config.config_dict['pause_fps']
    used_fps = config.config_dict['maxfps']

    if config.config_dict['fullscreen']:
        pygame.display.set_mode(config.config_dict['resolution'], pygame.FULLSCREEN)
    else:
        pygame.display.set_mode(config.config_dict['resolution'])
    pygame.display.set_caption(const.GAME_NAME)
    screen = pygame.display.get_surface()
    rect = screen.get_rect()
    fpsclock = FpsClock()
    sprite_container = SpriteManager()


def load_resources():
    global image_paths, sound_paths, images
    image_paths = do_resource_paths_dict('.png')
    sound_paths = do_resource_paths_dict('.ogg')
    images = load_images(image_paths)

def load_images(dict):
    images = {}
    for name, path in dict.items():
        images.update({name: pygame.image.load(path).convert()})
    return images

def do_resource_paths_dict(ext):
    images = {}
    for path in config.mods_paths:
        for item in os.listdir(path):
            if os.path.isfile(path + os.sep + item):
                if item.lower().endswith(ext):
                    images.update({item.rsplit(ext,1)[0]: path+'/'+item})
                    print(path+'/'+item, 'loaded.')
                    print(item.rsplit(ext,1)[0])

    for n, p in images.items():
        print(n, '\t', p)
    return images

def set_pause(bool):
    global  used_fps
    if bool:
        used_fps = pause_fps
    else:
        used_fps = config.config_dict['maxfps']

def render():
    global screen
    screen.fill((240,240,240))
    # Render.sprite_container.update()
    # Render.sprite_container.draw(Render.image)
    for id, name in metagame.MetaGame.game.images.items():
        # if metagame.MetaGame.game.positions[id].x <= Render.rect.width:
        #     if metagame.MetaGame.game.positions[id].y <= Render.rect.height:
                screen.blit(Render.images[name.name], (
                metagame.MetaGame.game.positions[id].x, metagame.MetaGame.game.positions[id].y))


    fpsclock.update(used_fps)
    screen.blit(fpsclock.image,(0,0))
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

    def register(self, image):
        self.add(Sprite(image))


    def update(self):
        super(SpriteManager, self).update()





class Sprite(pygame.sprite.DirtySprite):
    def __init__(self, image):
        super(Sprite, self).__init__()
        self.pos = (image._pos.xy)
        self.plane = image.plane

    def update(self):

        self.dirty = 1
        for group in self.groups():
            group.change_layer(self, self.layer)
        if self.scroll:
            self.rect.x = self.pos[0]+self.plane.camera.pos[0]
            self.rect.y = self.pos[1]+self.plane.camera.pos[1]


if __name__ == '__main__':
    print(do_resource_paths_dict('.png'))