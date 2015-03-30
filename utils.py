from __future__ import print_function
import os
import pygame
import render
import const




def click(mouse_pos, sprites):
    print('UTILS BEFORE FOR')
    for sprite in sprites:
        print('UTILS IN FOR')
        if sprite.rect.collidepoint(mouse_pos):
            sprite.on_click()

def label_surface(text, font_name=None, size=20, color=(150,10,150)):
    return pygame.font.Font(render.font_paths[font_name], size).render(text, 1, color)

def center_blit(mother, children):
    mother.blit(children, ((mother.get_width() - children.get_width()) / 2, (mother.get_height() - children.get_height()) / 2))


def load_image(full_path, color_key_pixel=(0, 0)):
    try:
        image = pygame.image.load(full_path)
    except pygame.error, message:
        print('Can\'t load image:', full_path)
        raise SystemExit, message
    image = image.convert()
    if color_key_pixel is not None:
        color_key = image.get_at(color_key_pixel)
        image.set_colorkey(color_key, pygame.RLEACCEL)
    return image


def make_grid_image(thicknes, color):
    side = 4 * const.GRID_SIZE + 2 * thicknes
    image = pygame.Surface((side, side)).convert()
    image.set_colorkey((0, 0, 0))
    pygame.draw.line(image, color, (0, 0), (side, 0), thicknes)
    pygame.draw.line(image, color, (0, const.GRID_SIZE), (side, const.GRID_SIZE), thicknes)
    pygame.draw.line(image, color, (0, 2 * const.GRID_SIZE), (side, 2 * const.GRID_SIZE), thicknes)
    pygame.draw.line(image, color, (0, 3 * const.GRID_SIZE), (side, 3 * const.GRID_SIZE), thicknes)
    pygame.draw.line(image, color, (0, side), (side, side), thicknes)
    pygame.draw.line(image, color, (0, 0), (0, side), thicknes)
    pygame.draw.line(image, color, (const.GRID_SIZE, 0), (const.GRID_SIZE, side), thicknes)
    pygame.draw.line(image, color, (2 * const.GRID_SIZE, 0), (2 * const.GRID_SIZE, side), thicknes)
    pygame.draw.line(image, color, (3 * const.GRID_SIZE, 0), (3 * const.GRID_SIZE, side), thicknes)
    pygame.draw.line(image, color, (side, 0), (side, side), thicknes)
    return image

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




