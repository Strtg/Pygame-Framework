import os
import defaults
_DIR = 'cfg' #  directory for config data
_ASSIGN_CHAR = '='
_NEW_LINE_CHAR = ';'

class Configurator(dict):
    def __init__(self, filename):
        self.filename = filename
        self.fullpath = os.path.join(_DIR, self.filename)

        self.update(defaults.make(self.filename))

    def _create_directory_if_needed(self):
        if os.path.isdir(_DIR) is False:
            print 'Directory', _DIR, 'doesn\'t exist.'
            os.mkdir(_DIR)
            print 'os.mkdir(_DIR)'
            print 'So',_DIR, 'directory created.'
        else:
            print 'Directory', _DIR, 'exists.'

    def _create_file_if_needed(self):
        if os.path.isfile(self.fullpath) is False:
            print 'File', self.filename, 'in directory', _DIR, 'doesn\'t exist'
            pass
        else:
            print 'OK'

