import manager
import pygame

class Game(object):
    def __init__(self, renderer, configurator):
        self.is_pause = False
        self.r = renderer
        self.c = configurator


        self.m = manager.Manager()
        self._init_objects()




    def _init_objects(self):
        pass

    def update(self):
        if self.is_pause:
            self.r.set_pause(True)
        else:
            pass