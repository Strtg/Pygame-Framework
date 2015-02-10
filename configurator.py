from __future__ import print_function
import os
import defaults
import const

class Configurator(object):
    def __init__(self):
        self._check_dirs()
        self._check_file(const.CONFIG_FILE)
        self._check_file(const.KEYS_FILE)
        self.configs = {}
        self.keys = {}
        self.reconfigure_from_files()


    def _reconfigure_from_files(self, dict, file):
        print('Loading data from', file +'...')

    def reconfigure_from_files(self):
        self._reconfigure_from_files(self.configs, const.CONFIG_DIR + os.sep + const.CONFIG_FILE)
        self._reconfigure_from_files(self.keys, const.CONFIG_DIR + os.sep + const.KEYS_FILE)



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



