"""
The module for contains and for setup/configuration functions.

This module contain file names, directory names and game name.
"""
import os

#############################################
# THOSE ARE CONSTANTS AND WILL NEVER CHANGE #
# SO THEY ARE GLOBAL                        #
#############################################

# Pathname separator
sep = os.sep

# Directory names.
MODS = 'mods'
VANILLA = 'vanilla'
IN = 'backend'
OUT = 'frontend'
GFX = 'gfx'
SND = 'sound'
CONFIG = 'config'
SAVES = 'saves'

# game name - printed on the title bar of the program
GAME_NAME = 'Game Pattern (refactoring branch)'

# save files extensions
SAVE_EXT = '.savgam'

# The directory tree for unmodded game
MOD_DIR = MODS  # MOD_DIR is better name than MODS
VANILLA_DIR = MOD_DIR + sep + VANILLA  # path to the directory for unmodified game
IN_DIR = VANILLA_DIR + sep + IN  # path to the directory for back-end game data like monster or item statistics
# that can be modded but required a new game to work
OUT_DIR = VANILLA_DIR + sep + OUT # the directory for front-end game data like graphics and sounds that can be safely modify
GFX_DIR = OUT_DIR + sep + GFX  # the directory for images
SND_DIR = OUT_DIR + sep + SND  # the directory for sound
CONFIG_DIR = CONFIG  # the directory for configuration files
SAVE_DIR = SAVES  # the directory for saved game files

# Basic file paths
CONFIG_FILE = CONFIG_DIR + sep + 'config.txt'  # the name of file for configuration data (game options)
KEYS_FILE = CONFIG_DIR + sep + 'keys.txt'  # The name of file for
MODS_FILE = MOD_DIR + sep + 'active_mods.txt'

# special characters in config files
CONFIG_SEPS = (':', '#')  # (name-value separator, comment)


