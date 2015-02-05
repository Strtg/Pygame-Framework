import os
_DIR = 'cfg' #  directory for config data
_ASSIGN_CHAR = '='
_NEW_LINE_CHAR = ';'

class Configurator(dict):
    def __init__(self, filename):
        self.filename = filename
        self.fullpath = os.path.join(_DIR, self.filename)
        if os.path.isdir(_DIR) is False:
            print 'Directory', _DIR, 'doesn\'t exist.'
            os.mkdir(_DIR)
            print 'So',_DIR, 'directory created.'
        else:
            print 'katalog', _DIR, 'istnieje'
            if os.path.isfile(self.fullpath) is False:
                print 'plik', self.filename, 'w katalogu', _DIR, 'doesn\'t exist'
            else:
                print 'OK'

        self.update({'asd': 12, 'fs8876fd': 345345})
        print self['asd']
