from __future__ import print_function
import manager
import pygame
import pickle
import const
import os

class Game(object):
    def __init__(self, renderer, configurator):
        self.is_pause = False
        self.r = renderer
        self.c = configurator
        self.info = ''
        self.info2 = ''


        self.m = manager.Manager()
        self._init_objects()

    def save(self):
        f = open(const.SAVE_DIR + os.sep + 'savedgame', 'wb')
        pickler = pickle.Pickler(f, 2)
        pickler.dump(self.info)
        pickler.dump(self.info2)
        f.close()
        del pickler

    def load(self):
        f = open(const.SAVE_DIR + os.sep + 'savedgame', 'rb')
        unpickler = pickle.Unpickler(f)
        self.info = unpickler.load()
        self.info2 = unpickler.load()
        f.close()
        del unpickler


    def _init_objects(self):
        pass

    def update(self):
        if self.is_pause:
            self.r.set_pause(True)
        else:
            pass

    def show_info(self):
        print (self.info)
        print (self.info2)


    def switch_pause(self):
        if self.is_pause:
            self.is_pause = False
            self.r.set_pause(False)
        else:
            self.is_pause = True
            self.r.set_pause(True)
