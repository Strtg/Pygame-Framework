import pygame
from config import Config as C

class Render(object):
    pause_fps = 5
    normal_fps = 10
    used_fps = normal_fps
    flags = 0
    fullscreen = 0
    image = None
    rect = None
    images = []  # container for images
    sounds = []
    fpsclock = None
    sprite_container = None

    @staticmethod
    def setup():
        Render.used_fps = C.config_dict['maxfps']
        Render.pause_fps = 5
        Render.images = []  # container for images
        Render.sprite_container = pygame.sprite.LayeredDirty()
        normal_fps = c.configs['maxfps']
        fpsclock = FpsClock()
        fullscreen = c.configs['fullscreen']
        if fullscreen:
            flags = flags | pygame.FULLSCREEN
        pygame.display.set_mode((c.configs['resolution']), flags)
        for img in images:
            C.loaded_images[img].image.convert()
        pygame.display.set_caption(config.GAME_NAME)

        image = pygame.display.get_surface()
        rect = image.get_rect()
        images = load_images()

    @staticmethod
    def load_resources():
        pass



    def load_images(self):
        return []


    def set_pause(self, bool):
        if bool:
            self.used_fps = self.pause_fps
        else:
            self.used_fps = self.normal_fps

    def render(self):
        self.sprite_container.update()

        # self.image.fill((90,0,0))
        self.sprite_container.draw(self.image)
        self.fpsclock.update(self.used_fps)
        self.image.blit(self.fpsclock.image,(0,0))
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


