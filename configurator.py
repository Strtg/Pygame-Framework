from __future__ import print_function
import os
import defaults
from const import *



class Configurator(object):
    def __init__(self):
        self.missing_dirs = []
        self._check_dirs()

    def _check_dirs(self):
        self.missing_dirs = []
        print ('')
        for d in defaults.dir_tree():
            if os.path.isdir(d):
                print ('OK:\t\t', d, 'exists.')

            else:
                print ('WARNING:', d, 'not exists.')
                self._create_dir(d)

    def _create_dir(self, d):
        os.mkdir(d)

        print ('\t\t', d, 'created.')


