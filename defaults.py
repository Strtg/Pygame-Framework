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
    t = (   'maxfps: 200;\r\n',
            'resolution: (400, 300);\r\n',
            'fullscreen: 0;\r\n',
            'debug: 0;\r\n',
    )
    return t

def keys():
    """
    Returns hardcoded tuple of strings with keys configuration.

    Used when the keys file doesn't exist.
    """
    t = (  'K_p: pause;\r\n',
            'K_ESCAPE: quit;\r\n',
            'QUIT: quit;\r\n',
            'K_q: quit;\r\n',
    )
    return t

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