import pygame
import const

class Renderer(object):


    def __init__(self, screen_size, fullscreen=False, fps=2000):
        self.used_fps = fps
        self.pause_fps = 5
        self.reconfigure(screen_size, fullscreen, fps)
        self.sprite_container = pygame.sprite.LayeredUpdates()


    def reconfigure(self, screen_size, fullscreen=False, fps=2000):
        self.flags = 0
        self.normal_fps = fps
        self.fpsclock = pygame.time.Clock()
        self.fullscreen = fullscreen
        if self.fullscreen:
            self.flags = self.flags | pygame.FULLSCREEN
        pygame.display.set_mode((screen_size), self.flags)
        pygame.display.set_caption(const.GAME_NAME)

        self.image = pygame.display.get_surface()
        self.rect = self.image.get_rect()

    def set_pause(self,bool):
        if bool:
            self.used_fps = self.pause_fps
        else:
            self.used_fps = self.normal_fps

    def render(self):
        self.sprite_container.update()

        self.image.fill((90,0,0))
        self.sprite_container.draw(self.image)
        self.fpsclock.tick(self.used_fps)
        pygame.display.flip()





