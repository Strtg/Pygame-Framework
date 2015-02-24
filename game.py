from __future__ import print_function
import pickle

from config import SAVES
from config import Config as C
from render import Render as R
import os
import datetime
import game_object
import layers
from debugator import debugator



class Game(object):
    is_pause = False
    name = None
    difficulty = None
    date_of_creating = datetime.datetime.now()
    m = None  # object manager

    @staticmethod
    @debugator
    def new(name='New Game created by new_game() function!!!', difficulty='normal'):
        Game.is_pause = False
        Game.name = name
        Game.difficulty = difficulty
        Game.date_of_creating = datetime.datetime.now()
        Game.m = Manager()  # object manager
        print ('NEW GAME!!!')

        Game.x0 = game_object.Visible()
        Game.x1 = game_object.Object()
        Game.x2 = game_object.Visible()
        Game.x3 = game_object.Object()
        Game.x4 = game_object.Visible()
        Game.x5 = game_object.Object()

        print(Game.x0.id)
        print(Game.x1.id)
        print(Game.x2.id)
        print(Game.x3.id)
        print(Game.x4.id)
        print(Game.x5.id)


    @staticmethod
    @debugator
    def save():
        f = open(SAVES + os.sep + 'savedgame', 'wb')
        pickler = pickle.Pickler(f, 2)
        pickler.dump(Game.is_pause)
        pickler.dump(Game.name)
        pickler.dump(Game.difficulty)
        pickler.dump(Game.date_of_creating)


        f.close()
        del pickler

    @staticmethod
    @debugator
    def load():
        f = open(SAVES + os.sep + 'savedgame', 'rb')
        unpickler = pickle.Unpickler(f)
        Game.is_pause = unpickler.load()
        Game.name = unpickler.load()
        Game.difficulty = unpickler.load()
        Game.date_of_creating = unpickler.load()

        f.close()
        del unpickler


    @staticmethod
    # @debugator
    def update():
        if Game.is_pause:
            pass
        else:
            pass

    @staticmethod
    @debugator
    def show_info():
        print (Game.name)
        print (Game.difficulty)
        print (Game.date_of_creating)

    @staticmethod
    @debugator
    def switch_pause():
        if Game.is_pause:
            Game.is_pause = False
            R.set_pause(False)
        else:
            Game.is_pause = True
            R.set_pause(True)


class Manager(object):
    """
    Object manager.
    """
    @debugator
    def __init__(self):
        self.objects = []
