import os
#############################################
# THOSE ARE CONSTANTS AND WILL NEVER CHANGE #
# UNLESS YOU WANT TO CHANGE THE GAME CODE   #
# SO THEY ARE GLOBAL                        #
#############################################

# game name - printed on the title bar of the program
GAME_NAME = 'Game Pattern (refactoring branch)'

# save files extensions
SAVE_EXT = '.savgam'

# Pathname separator
sep = os.sep

# Directory names.
MODS = 'mods'
VANILLA = 'vanilla'
IN = 'backend'
OUT = 'frontend'
GFX = 'gfx'
SND = 'snd'
CONFIG = 'config'
SAVES = 'saves'

DIR_NAMES = {
    'backend': 'IN',
    'frontend': 'OUT',
    'gfx': 'GFX',
    'snd': 'SND'
}

# Basic file paths
CONFIG_FILE = CONFIG + sep + 'config.txt'  # the name of file for configuration data (game options)
KEYS_DOWN_FILE = CONFIG + sep + 'keys_down.txt'  # The name of file for
KEYS_UP_FILE = CONFIG + sep + 'keys_up.txt'  # The name of file for

MODS_FILE = MODS + sep + 'active_mods.txt'

# special characters in config files
CONFIG_SEPS = (':', '#')  # (name-value separator, comment)

# directory structure
SUB_DIR_TREE = {
    'IN': IN,
    'OUT': OUT,
    'GFX': OUT + sep + GFX,
    'SND': OUT + sep + SND
}

BASIC_DIR_TREE = (
    CONFIG,  # the directory for configuration files
    SAVES,  # the directory for saved game files
    MODS,  # mods_paths dir
    MODS + sep + VANILLA,  # path to the directory for unmodified game
    MODS + sep + VANILLA + sep + SUB_DIR_TREE['IN'],
    # path to the directory for back-end game data like monster or item statistics
    # that can be modded but required a new game to work
    MODS + sep + VANILLA + sep + SUB_DIR_TREE['OUT'],
    # the directory for front-end game data like graphics and sounds that can be safely modify
    MODS + sep + VANILLA + sep + SUB_DIR_TREE['GFX'],  # the directory for images
    MODS + sep + VANILLA + sep + SUB_DIR_TREE['SND']  # the directory for sound
)

# default hardcoded configuration files
DEFAULT_CONFIG_FILE = [
    {'key': 'maxfps', 'value': '1000'},
    {'key': 'resolution', 'value': '1366, 768'},
    {'key': 'game_logic_speed', 'value': '0.001'},
    {'key': 'fullscreen', 'value': '0'},
    {'key': 'camera_speed', 'value': '0.5'},
    {'key': 'pause_fps', 'value': '1'},

]

DEFAULT_KEYS_DOWN_FILE = [
    {'key': 'K_ESCAPE', 'value': 'main_menu'},
    {'key': 'K_p', 'value': 'pause'},
    {'key': 'QUIT', 'value': 'quit'},
    {'key': 'K_q', 'value': 'quit'},
    {'key': 'K_s', 'value': 'save'},
    {'key': 'K_l', 'value': 'load'},
    {'key': 'K_i', 'value': 'show_info'},
    {'key': 'K_f', 'value': 'switch_fullscreen'},
    {'key': 'K_F5', 'value': 'reload_resources'},
    {'key': 'K_LEFT', 'value': 'view_left'},
    {'key': 'K_RIGHT', 'value': 'view_right'},
    {'key': 'K_UP', 'value': 'view_up'},
    {'key': 'K_DOWN', 'value': 'view_down'},
]

DEFAULT_KEYS_UP_FILE = [
    {'key': 'K_LEFT', 'value': 'camera_stop'},
    {'key': 'K_RIGHT', 'value': 'camera_stop'},
    {'key': 'K_UP', 'value': 'camera_stop'},
    {'key': 'K_DOWN', 'value': 'camera_stop'}
]

DEFAULT_MODS_FILE = [
    {'comment': 'type here mod names and what you want (which directory) from that mod'},
    {'comment': 'for example:'},
    {'comment': 'awsomemod_1.3: all  # means you want all from that mod'},
    {'comment': 'bigger_realism_0.1: frontend  # means you want only graphics and sounds from that mod'},
    {'comment': 'subdirectories of typed directory are automatically loaded'},
    {'comment': 'you can type more than one mod in new lines'},
    {'comment': 'you can type the same mod more than ine time which is useful'},
    {'comment': 'when you want to load more than one directories from the same mod'},
    {'comment': 'mods_paths are loaded one after another from top to bottom'},
    {'comment': 'when a more than one mod modify the same things the mod loaded later will overwrite previous mod'},
    {'comment': 'vanilla is always loaded as the first "mod" even when it is not typed here'}
]

if __name__ == '__main__':
    print DEFAULT_CONFIG_FILE[0]