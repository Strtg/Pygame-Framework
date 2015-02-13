import pygame
import const

class Renderer(object):

    def __init__(self, configurator):
        self.c = configurator
        self.used_fps = self.c.configs['maxfps']
        self.pause_fps = 1
        self.reconfigure()
        self.sprite_container = pygame.sprite.LayeredDirty()


    def reconfigure(self):

        self.flags = 0
        self.normal_fps = self.c.configs['maxfps']
        self.fpsclock = FpsClock()
        self.fullscreen = self.c.configs['fullscreen']
        if self.fullscreen:
            self.flags = self.flags | pygame.FULLSCREEN
        pygame.display.set_mode((self.c.configs['resolution']), self.flags)
        pygame.display.set_caption(const.GAME_NAME)

        self.image = pygame.display.get_surface()
        self.rect = self.image.get_rect()

    def set_pause(self, bool):
        if bool:
            self.used_fps = self.pause_fps
        else:
            self.used_fps = self.normal_fps

    def render(self):
        self.sprite_container.update()

        self.image.fill((90,0,0))
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


