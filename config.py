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
SND = 'sound'
CONFIG = 'config'
SAVES = 'saves'

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
    MODS,  # mods dir
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
DEFAULT_CONFIG_FILE = (
    'maxfps: 100',
    'resolution: 400, 400',
    'fullscreen: 0',
    'debug: 0'
)

DEFAULT_KEYS_FILE = (
    'K_ESCAPE: main_menu',
    'K_p: pause',
    'QUIT: quit',
    'K_q: quit',
    'K_s: save',
    'K_l: load',
    'K_i: show_info'
)

DEFAULT_MODS_FILE = (
    '# type here mod names and what you want (which directory) from that mod',
    '# for example:',
    '# awsomemod_1.3: all  # means you want all from that mod',
    '# bigger_realism_0.1: frontend  # means you want only graphics and sounds from that mod',
    '# subdirectories of typed directory are automatically loaded',
    '# you can type more than one mod in new lines',
    '# you can type the same mod more than ine time which is useful',
    '# when you want to load more than one directories from the same mod',
    '# mods are loaded one after another from top to bottom',
    '# when a more than one mod modify the same things the mod loaded later will overwrite previous mod',
    '# vanilla is always loaded as the first "mod" even when it is not typed here'
)

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


def put_defaults_in_file(filepath, content):
    pass


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


def do_file_from_list(list, filepath):  # returns None
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


#################################
# BASIC SETUP STUFF             #
#################################
def setup():  # returns None
    # create directory if needed
    for dir in BASIC_DIR_TREE:
        if check_if_directory_exists(dir) == False:
            create_directory(dir)

    # create files if needed
    if check_if_file_exists(CONFIG_FILE) == False:
        put_defaults_in_file(CONFIG_FILE)
        put_defaults_in_file(CONFIG_FILE, DEFAULT_CONFIG_FILE)
    if check_if_file_exists(KEYS_FILE) == False:
        create_file(KEYS_FILE)
        put_defaults_in_file(KEYS_FILE, DEFAULT_KEYS_FILE)
    if check_if_file_exists(MODS_FILE) == False:
        create_file(MODS_FILE)
        put_defaults_in_file(MODS_FILE, DEFAULT_MODS_FILE)


class Config(object):
    """
    All methods are static, because there are no need to have more
    than one instances of this class. I don't want to modify globals
    in my functions so it is a class.

    raw_list is a list made from file as it is
    pure_list is made from raw_list with deleting comments and blank lines

    to do:
    read file to a raw list
    make purelist
    update dict with purelist
    """
    config_from_file = []  # list of dictionaries {'key':'string', 'value':'string', 'comment':'string'}
    keys_from_file = []
    mods_from_file = []

    config_dict = {}  # clean config_from_file (no comments, just keys and values), flat dictionary
    keys_dict = {}
    mods_list = []



