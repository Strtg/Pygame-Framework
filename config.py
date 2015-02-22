from __future__ import print_function
import os

"""
The module for contains and for setup/configuration functions.

This module contain file names, directory names and game name.
"""


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
KEYS_FILE = CONFIG + sep + 'keys.txt'  # The name of file for
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
    {'key': 'maxfps', 'value': '100'},
    {'key': 'resolution', 'value': '400, 400'},
    {'key': 'fullscreen', 'value': '0'},
    {'key': 'debug', 'value': '0'}
]

DEFAULT_KEYS_FILE = [
    {'key': 'K_ESCAPE', 'value': 'main_menu'},
    {'key': 'K_p', 'value': 'pause'},
    {'key': 'QUIT', 'value': 'quit'},
    {'key': 'K_q', 'value': 'quit'},
    {'key': 'K_s', 'value': 'save'},
    {'key': 'K_l', 'value': 'load'},
    {'key': 'K_i', 'value': 'show_info'},
    {'key': 'K_F5', 'value': 'reload_resources'}
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

########################
# FUNCTION DEFINITIONS #
########################


def check_if_directory_exists(dirpath):
    print('Checking directory: {0} ...'.format(dirpath))
    if os.path.isdir(dirpath):
        print('OK, {0} exists.'.format(dirpath))
        return True
    else:
        print('Warning:, {0} not exists.'.format(dirpath))
        return False


def create_directory(dirpath):
    os.mkdir(dirpath)
    print('Directory {0} created'.format(dirpath))


def check_if_file_exists(filepath):
    print('Checking file: {0} ...'.format(filepath))
    if os.path.isfile(filepath):
        print('OK, {0} exists.'.format(filepath))
        return True
    else:
        print('Warning:, {0} not exists.'.format(filepath))
        return False


def create_file(filepath):
    file = open(filepath, 'w')
    file.close()
    print('File {0} created'.format(filepath))


def do_list_from_file(filepath):  # returns a list of dicts
    # load to list
    raw_list = []
    file = open(filepath)
    for line in file:
        raw_list.append(line)
    file.close()
    # make list with separate comments
    dict_list = []
    for line in raw_list:
        new_line = {}
        comment = None
        key = None
        value = None
        divided_line = line.split(CONFIG_SEPS[1], 1)
        if len(divided_line) > 1:
            comment = divided_line[1].strip() # this is comment
            if len(divided_line[0].split(CONFIG_SEPS[0], 1)) > 1:
                key = divided_line[0].split(CONFIG_SEPS[0], 1)[0].strip()
                value = divided_line[0].split(CONFIG_SEPS[0], 1)[1].strip()
        else:
            if len(divided_line[0].split(CONFIG_SEPS[0], 1)) > 1:
                key = divided_line[0].split(CONFIG_SEPS[0], 1)[0].strip()
                value = divided_line[0].split(CONFIG_SEPS[0], 1)[1].strip()
        if key is not None:
            new_line.update({'key': key})
        if value is not None:
            new_line.update({'value': value})
        if comment is not None:
            new_line.update({'comment': comment})
        dict_list.append(new_line)
    return dict_list


def do_file_from_list(filepath, list):  # returns None
    lines_to_write = []
    for line in list:
        line_to_write = ''
        if 'key' in line:
            line_to_write += (line['key'] + CONFIG_SEPS[0] + ' ')
        if 'value' in line:
            line_to_write += line['value']
        if 'comment' in line:
            if 'key' in line:
                line_to_write += ('  ' + CONFIG_SEPS[1] + ' ' + line['comment'])
            else:
                line_to_write += (CONFIG_SEPS[1] + ' ' + line['comment'])
        line_to_write += os.linesep
        lines_to_write.append(line_to_write)
    file = open(filepath, 'w')
    file.writelines(lines_to_write)
    file.close()


def do_dict_from_list(list):  # returns dictionary
    dictionary = {}
    for d in list:
        if 'key' in d:
            dictionary.update({d['key']: d['value']})
    # convert to ints and tuples
    for key in dictionary:
        if dictionary[key].isdigit():
            dictionary[key] = int(dictionary[key])
        elif ',' in dictionary[key]:
            dictionary[key] = map(int, dictionary[key].split(','))
    return dictionary


def upgrade_dict_from_list(dict, list):  # returns None
    for d in list:
        if 'key' in d:
            dict.update({d['key']: d['value']})
    # convert to ints and tuples
    for key in dict:
        if dict[key].isdigit():
            dict[key] = int(dict[key])
        elif ',' in dict[key]:
            dict[key] = map(int, dict[key].split(','))


def upgrade_list_from_dict(list, dict):  # returns None
    for key, value in dict.items():
        for line in list:
            if 'key' in line:
                if key == line['key']:
                    if ',' in str(value):
                        line['value'] = str(value)[1:-1]
                    else:
                        line['value'] = str(value)

def do_mods(_):  # returns list of paths
    mods = []
    for line in _:
        if 'key' in line:
            mods.append({'name': line['key'], 'dir': line['value']})
    # now make list of fullpaths
    paths = []
    for line in mods:
        path = MODS + sep + line['name']
        if line['dir'] != 'all':
            for name in DIR_NAMES:
                if name == line['dir']:
                    # print( SUB_DIR_TREE[DIR_NAMES[name].upper()] )
                    path += sep + SUB_DIR_TREE[DIR_NAMES[name].upper()]
        paths.append(path)
    print(paths)
    # now make list of all fullpaths!
    all_paths = []
    for path in paths:
        for tup in os.walk(path):
            all_paths.append(tup[0])
    print(all_paths)
    return all_paths





    return paths

#################################
#    CLASS CONFIG               #
#################################


class Config(object):
    """
    All methods are static, because there are no need to have more
    than one instances of this class. I don't want to modify globals
    in my functions so it is a class.
    """
    config_list = []  # list of dictionaries {'key':'string', 'value':'string', 'comment':'string'}
    keys_list = []
    mods_list = []

    config_dict = {}  # clean config_from_file (no comments, just keys and values), flat dictionary
    keys_dict = {}
    mods_paths = ['kurwa']  # list of dictionaries (name, fullpath)


    @staticmethod
    def setup():  # returns None
        # create directory if needed
        for dir in BASIC_DIR_TREE:
            if check_if_directory_exists(dir) == False:
                create_directory(dir)
        # create files if needed
        if check_if_file_exists(CONFIG_FILE) == False:
            create_file(CONFIG_FILE)
            do_file_from_list(CONFIG_FILE, DEFAULT_CONFIG_FILE)
        if check_if_file_exists(KEYS_FILE) == False:
            create_file(KEYS_FILE)
            do_file_from_list(KEYS_FILE, DEFAULT_KEYS_FILE)
        if check_if_file_exists(MODS_FILE) == False:
            create_file(MODS_FILE)
            do_file_from_list(MODS_FILE, DEFAULT_MODS_FILE)


    @staticmethod
    def load_config():
        Config.config_list = do_list_from_file(CONFIG_FILE)
        Config.keys_list = do_list_from_file(KEYS_FILE)
        Config.mods_list = do_list_from_file(MODS_FILE)
        Config.config_dict = do_dict_from_list(Config.config_list)
        Config.keys_dict = do_dict_from_list(Config.keys_list)
        Config.mods_paths = do_mods(Config.mods_list)


    @staticmethod
    def save_config():
        upgrade_list_from_dict(Config.config_list, Config.config_dict)
        upgrade_list_from_dict(Config.keys_list, Config.keys_dict)
        do_file_from_list(CONFIG_FILE, Config.config_list)
        do_file_from_list(KEYS_FILE, Config.keys_list)


    @staticmethod
    def print_sep():
        print(CONFIG_SEPS)


