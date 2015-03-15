from __future__ import print_function
import os
import pygame


def load_image(full_path, color_key_pixel=None):
    try:
        image = pygame.image.load(full_path)
    except pygame.error, message:
        print('Can\'t load image:', full_path)
        raise SystemExit, message
    image = image.convert()
    if color_key_pixel is not None:
        color_key = image.get_at(color_key_pixel)
        image.set_colorkey(color_key, pygame.RLEACCEL)
    return image, image.get_rect()





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




