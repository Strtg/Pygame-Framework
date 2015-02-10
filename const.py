"""
The module with constants.

This module contain file names, directory names and game name.
"""

# game name
GAME_NAME = 'Basic Framework Made of Pygame'

# directories
MOD_DIR = 'mods'
OUT_DIR = 'frontend'  # the directory for front-end game data like graphics and sounds that can be safely modify
IN_DIR = 'backend'  # the directory for back-end game data like monster or item statistics
# that can be modded but required a new game to work
VANILLA_DIR = 'vanilla'  # the directory for unmodified game
CONFIG_DIR = 'config'  # the directory for configuration files
SAVE_DIR = 'saves'  # the directory for saved game files
GFX_DIR = 'gfx'  # the directory for images for sprites
SND_DIR = 'sound'  # the directory for sound

# files
CONFIG_FILE = 'config.txt'  # the name of file for configuration data (game options)
KEYS_FILE = 'keys.txt'  # The name of file for
CONFIG_FILE_FORMAT = ('=',';','#')  # (name-value separator, end line, comment)