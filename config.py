from __future__ import print_function
import os

import utils
import const


"""
The module for contains and for setup/configuration functions.

This module contain file names, directory names and game name.
"""

config_list = []  # list of dictionaries {'key':'string', 'value':'string', 'comment':'string'}
keys_down_list = []
keys_up_list = []
mods_list = []
config_dict = {}  # clean config_from_file (no comments, just keys and values), flat dictionary
keys_down_dict = {}
keys_up_dict = {}
mods_paths = []  # list of dictionaries (name, fullpath)




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
        divided_line = line.split(const.CONFIG_SEPS[1], 1)
        if len(divided_line) > 1:
            comment = divided_line[1].strip() # this is comment
            if len(divided_line[0].split(const.CONFIG_SEPS[0], 1)) > 1:
                key = divided_line[0].split(const.CONFIG_SEPS[0], 1)[0].strip()
                value = divided_line[0].split(const.CONFIG_SEPS[0], 1)[1].strip()
        else:
            if len(divided_line[0].split(const.CONFIG_SEPS[0], 1)) > 1:
                key = divided_line[0].split(const.CONFIG_SEPS[0], 1)[0].strip()
                value = divided_line[0].split(const.CONFIG_SEPS[0], 1)[1].strip()
        if key is not None:
            new_line.update({'key': key})
        if value is not None:
            new_line.update({'value': value})
        if comment is not None:
            new_line.update({'comment': comment})
        dict_list.append(new_line)
    return dict_list

def do_file_from_list(filepath, list):  # returns None
    print('bede robic plik')
    print(list)
    lines_to_write = []
    for line in list:
        print(line)
        line_to_write = ''
        if 'key' in line:
            line_to_write += (line['key'] + const.CONFIG_SEPS[0] + ' ')
        if 'value' in line:
            line_to_write += line['value']
        if 'comment' in line:
            if 'key' in line:
                line_to_write += ('  ' + const.CONFIG_SEPS[1] + ' ' + line['comment'])
            else:
                line_to_write += (const.CONFIG_SEPS[1] + ' ' + line['comment'])
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
        elif '.' in dictionary[key]:
            dictionary[key] = float(dictionary[key])

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
    mods.append({'name': const.VANILLA, 'dir': 'all'})  # sneaky vanilla game adding
    for line in _:
        if 'key' in line:
            mods.append({'name': line['key'], 'dir': line['value']})
    # now make list of fullpaths
    paths = []
    for line in mods:
        path = const.MODS + os.sep + line['name']
        if line['dir'] != 'all':
            for name in const.DIR_NAMES:
                if name == line['dir']:
                    # print( SUB_DIR_TREE[DIR_NAMES[name].upper()] )
                    path += os.sep + const.SUB_DIR_TREE[const.DIR_NAMES[name].upper()]
        paths.append(path)
    print(paths)
    # now make list of all fullpaths!
    all_paths = []
    for path in paths:
        for tup in os.walk(path):
            all_paths.append(tup[0])
    print(all_paths)
    return all_paths




def setup():  # returns None
    # create directory if needed
    for dir in const.BASIC_DIR_TREE:
        if utils.check_if_directory_exists(dir) == False:
            utils.create_directory(dir)
    # create files if needed
    if utils.check_if_file_exists(const.CONFIG_FILE) == False:
        utils.create_file(const.CONFIG_FILE)
        do_file_from_list(const.CONFIG_FILE, const.DEFAULT_CONFIG_FILE)
    if utils.check_if_file_exists(const.KEYS_DOWN_FILE) == False:
        utils.create_file(const.KEYS_DOWN_FILE)
        do_file_from_list(const.KEYS_DOWN_FILE, const.DEFAULT_KEYS_DOWN_FILE)
    if utils.check_if_file_exists(const.KEYS_UP_FILE) == False:
        utils.create_file(const.KEYS_UP_FILE)
        do_file_from_list(const.KEYS_UP_FILE, const.DEFAULT_KEYS_UP_FILE)
    if utils.check_if_file_exists(const.MODS_FILE) == False:
        utils.create_file(const.MODS_FILE)
        do_file_from_list(const.MODS_FILE, const.DEFAULT_MODS_FILE)


def load_config():
    config_list = do_list_from_file(const.CONFIG_FILE)
    keys_down_list = do_list_from_file(const.KEYS_DOWN_FILE)
    keys_up_list = do_list_from_file(const.KEYS_UP_FILE)
    mods_list = do_list_from_file(const.MODS_FILE)
    config_dict = do_dict_from_list(config_list)
    keys_down_dict = do_dict_from_list(keys_down_list)
    keys_up_dict = do_dict_from_list(keys_up_list)
    mods_paths = do_mods(mods_list)


def save_config():
    upgrade_list_from_dict(config_list, config_dict)
    upgrade_list_from_dict(keys_down_list, keys_down_dict)
    upgrade_list_from_dict(keys_up_list, keys_up_dict)
    do_file_from_list(const.CONFIG_FILE, config_list)
    do_file_from_list(const.KEYS_DOWN_FILE, keys_down_list)
    do_file_from_list(const.KEYS_UP_FILE, keys_up_list)


if __name__ == '__main__':
    setup()