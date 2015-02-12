"""
Module with just two simply function to create default content for configuration files.

Used when configuration files can not be used for some reasons.
"""
from os import sep
from const import *

def config():
    """
    Returns hardcoded tuple of strings with configuration data.

    Used when the configuration file doesn't exist.
    """
    d = {   'maxfps': 10,
            'resolution': (400, 400),
            'fullscreen': 0,
            'debug': 0
        }
    return d

def keys():
    """
    Returns hardcoded tuple of strings with keys configuration.

    Used when the keys file doesn't exist.
    """
    d = {  'K_p': 'pause',
            'K_ESCAPE': 'quit',
            'QUIT': 'quit',
            'K_q': 'quit'
        }
    return d

def dir_tree():
    """
    Basic directories of the game.
    :return: tuple of strings
    """
    t = (   CONFIG_DIR +sep,
            MOD_DIR +sep,
            MOD_DIR +sep+ VANILLA_DIR +sep,
            MOD_DIR +sep+ VANILLA_DIR +sep+ OUT_DIR +sep,
            MOD_DIR +sep+ VANILLA_DIR +sep+ OUT_DIR +sep+ GFX_DIR +sep,                MOD_DIR+sep+VANILLA_DIR+sep+OUT_DIR+sep+SND_DIR+sep,
            MOD_DIR +sep+ VANILLA_DIR +sep+ IN_DIR +sep,
            SAVE_DIR +sep
    )
    return t