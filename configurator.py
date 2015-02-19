from __future__ import print_function
import os
import defaults
import const
import game_sprite

class Configurator(object):
    def __init__(self):
        self.configs = {}  # all here is made just for this sucker
        self.keys = {}  # and this
        self.loaded_images = {}
        self.images_paths = []
        self.configs_from_file = {}
        self.keys_from_file = {}
        self.active_mods = []


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

        self.active_mods = self.load_active_mods()

        self.loaded_images = self.load_images()

    def load_active_mods(self):
        print('FUNKCJA LOAD_ACTIVE_MODS')
        alist = []
        f = open(const.MOD_DIR + os.sep + const.ACTIVE_MODS)
        for l in f:
            e = l.split(const.CONFIG_SEPS[1])[0].strip()  # hope it is key and value
            if e:
                print('to nie komentarz!')
                print(e)
                notempty = e.split(const.CONFIG_SEPS[0])  # this is list of two elements: key and value
                mod_name = notempty[0].strip()
                mod_subdir = notempty[1].strip()
                print('mod to:', mod_name)
                print('katalog to:', mod_subdir)
                if mod_subdir == '' or mod_subdir == 'all':
                    alist.append(const.MOD_DIR + os.sep + mod_name)
                    print('znaleziono mod do calkowitego wladowania.')
                    print('lista wyglada tak', alist)
                else:
                    print('jest to jebane else czy nie?', mod_name)
                    for root, dirs, files in os.walk(const.MOD_DIR + os.sep + mod_name):
                        print('jest else', root, dirs, files)
                        for dir in dirs:
                            print('test if:', dir, mod_subdir)
                            if dir == mod_subdir:
                                alist.append(root + os.sep +dir)
        f.close()
        print ('ACTIVE MODS: ', alist)
        return alist


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

    def find_files_deep(self, directory, extension=''):
        list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    list.append(os.path.join(root, file))
        return list



    def load_images(self):
        self.loaded_images = {}
        gfx_dir = const.MOD_DIR + os.sep + const.VANILLA_DIR + os.sep +\
                        const.OUT_DIR + os.sep + const.GFX_DIR
        dirtree = [i for i in os.walk(gfx_dir)]
        print (dirtree[0][2])
        filepaths = []
        for tup in dirtree:
            if tup[2]:
                for fil in tup[2]:
                    if fil.endswith('.png'):
                        filepaths.append(tup[0] + os.sep + fil)
        print('znalezione:')
        print(filepaths)
        for path in filepaths:
            print(path)
            print(path.rsplit(os.sep, 1)[-1])
            self.loaded_images.update({path.rsplit(os.sep, 1)[-1].rsplit('.png')[0]:game_sprite.Sprite(path)})
        print (self.loaded_images)


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



