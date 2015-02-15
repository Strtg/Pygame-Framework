from __future__ import print_function
import manager
import pygame
import pickle
import const
import os
import datetime
import game_object
import layers

class Game(object):
    def __init__(self, renderer, configurator, name='Unnamed game', difficulty='normal'):
        # will this work?
        self.r = renderer
        self.c = configurator
        # create new game state
        self.new_game()

    def new_game(self, name='New Game created by new_game() function!!!', difficulty='normal'):
        self.is_pause = False
        self.name = name
        self.difficulty = difficulty
        self.date_of_creating = datetime.datetime.now()
        self.objects = []
        self._init_objects()
        self.m = manager.Manager()
        print ('NEW GAME!!!')

    def save(self):
        f = open(const.SAVE_DIR + os.sep + 'savedgame', 'wb')
        pickler = pickle.Pickler(f, 2)
        pickler.dump(self.is_pause)
        pickler.dump(self.name)
        pickler.dump(self.difficulty)
        pickler.dump(self.date_of_creating)
        pickler.dump(self.objects)


        f.close()
        del pickler

    def load(self):
        f = open(const.SAVE_DIR + os.sep + 'savedgame', 'rb')
        unpickler = pickle.Unpickler(f)
        self.is_pause = unpickler.load()
        self.name = unpickler.load()
        self.difficulty = unpickler.load()
        self.date_of_creating = unpickler.load()
        self.objects = unpickler.load()

        f.close()
        del unpickler



    def _init_objects(self):
        self.objects.append(game_object.Visible(l=layers.background, app='background'))
        self.objects.append(game_object.Visible(l=layers.interface, app='logo'))



    def update(self):
        if self.is_pause:
            self.r.set_pause(True)
        else:
            pass

    def show_info(self):
        print (self.name)
        print (self.difficulty)
        print (self.date_of_creating)
        print (self.objects)


    def switch_pause(self):
        if self.is_pause:
            self.is_pause = False
            self.r.set_pause(False)
        else:
            self.is_pause = True
            self.r.set_pause(True)
