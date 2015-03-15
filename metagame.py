from __future__ import print_function
import pickle
import os
import datetime

from const import SAVES
import config
# from temp import config
import game


class MetaGame(object):
    """
    The MetaGame class is something like a game manager.

    It starts new games, saves and loads games. It can pause the game.
    It should do things that can be done outside the game.
    To do: MetaGame should have container for commands inputed by player.
    """
    is_pause = False
    commands = []
    game = None

    @staticmethod
    def new(name='New Game created by new_game() function!!!', difficulty='normal'):
        MetaGame.is_pause = False
        MetaGame.name = name
        MetaGame.difficulty = difficulty
        MetaGame.date_of_creating = datetime.datetime.now()
        MetaGame.game = game.Game()  # object manager and game instance to save/load
        MetaGame.current_stage = MetaGame.game
        MetaGame.commands = []

        print ('NEW GAME!!!')

    @staticmethod
    def save():
        f = open(SAVES + os.sep + 'savedgame' + config.SAVE_EXT, 'wb')
        pickler = pickle.Pickler(f, 2)
        pickler.dump(MetaGame.game)
        f.close()
        del pickler

    @staticmethod
    def load():
        f = open(SAVES + os.sep + 'savedgame' + config.SAVE_EXT, 'rb')
        unpickler = pickle.Unpickler(f)
        MetaGame.game = unpickler.load()
        f.close()
        del unpickler


    @staticmethod
    def update():
        MetaGame.game.update()

    @staticmethod
    def show_info():
        print (MetaGame.game.name)
        print (MetaGame.game.difficulty)
        print (MetaGame.game.date_of_creating)

    @staticmethod
    def switch_pause():
        if MetaGame.is_pause:
            MetaGame.is_pause = False
            R.set_pause(False)
        else:
            MetaGame.is_pause = True
            R.set_pause(True)



