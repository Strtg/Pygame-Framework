from __future__ import print_function
import os
import defaults
import const
import re

class Configurator(object):
    def __init__(self):
        self.configs = {}  # all here is made just for this sucker
        self.keys = {}  # and this
        self.configs_from_file = {}
        self.keys_from_file = {}

        print()
        self._check_dirs()
        print()
        self._check_file(const.CONFIG_FILE)
        self._check_file(const.KEYS_FILE)

        print()
        self.configs.update(defaults.config())  # load defaults config
        print(self.configs)
        self.keys.update(defaults.keys())  # load defaults keys
        print(self.keys)
        print()
        self._load_from_file(self.configs_from_file, const.CONFIG_DIR + os.sep + const.CONFIG_FILE)
        print(self.configs_from_file)
        self._load_from_file(self.keys_from_file, const.CONFIG_DIR + os.sep + const.KEYS_FILE)
        print(self.keys_from_file)

        # merge
        self.configs.update(self.configs_from_file)
        print('After merging:', self.configs)
        self.keys.update(self.keys_from_file)
        print('After merging:', self.keys)

    def _load_from_file(self, d, f):
        print('BEGINING OF LOAD', f + '...')
        d.clear()
        file = open(f)
        for s in file:  # in every file line do:
            e = s.split(const.CONFIG_SEPS[1])[0].strip()  # hope it is key and value
            print(e)
            if e:
                e = e.split(const.CONFIG_SEPS[0])  # this is list of two elements: key and value
                d.update({e[0].strip():e[1].strip()})
        file.close()
        print('Converting...')
        for e in d:
            if ',' in d[e]:  # coma in string means this should be tuple
                print ('come detected in', d[e])
                d[e] = tuple(map(int, d[e].split(',')))
            else:
                if d[e].isdigit():
                    d[e] = int(d[e])




    def _reconfigure_from_files(self, dict, file):
        print('Loading data from', file +'...')

    def _check_dirs(self):
        print ('Checking directories...')
        for d in defaults.dir_tree():
            if os.path.isdir(d):
                print ('OK:\t\t', d, 'exists.')
            else:
                print ('WARNING:', d, 'not exists.')
                self._create_dir(d)

    def _create_dir(self, d):
        os.mkdir(d)
        print ('\t\t', d, 'created.')

    def _check_file(self, f):
        print ('Checking', f, 'file...')
        f = const.CONFIG_DIR + os.sep + f
        if os.path.isfile(f):
            print ('OK:\t\t', f, 'exists.')
        else:
            print ('WARNING:', f, 'not exists.')
            self._create_file(f)

    def _create_file(self, f):
        file = open(f, 'w')
        file.close()
        print ('\t\t', f, 'created.')



