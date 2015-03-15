"""
Trying pure CES
what is done:
Position
Move
Image
Plane
"""
from __future__ import print_function
import pygame

class Component(object):

    def __init__(self):
        print('A new component: ', end='')

    def __str__(self):
        return 'Component '


class Position(Component):
    """
    x, y, z coordination. In some/most 2D games 'z' (height) can be ignored and left at zero, but sometimes can be useful.
    """
    def __init__(self, pos):
        super(Position, self).__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.old_x = pos[0]
        self.old_y = pos[1]
        self.old_z = pos[2]
        self.offset_x = 0
        self.offset_y = 0
        self.offset_z = 0
        print('Position is created')

    def __str__(self):
        return super(Position, self).__str__() + 'Position: x = {0}, y = {1}, z = {2}'.format(self.x, self.y, self.z)


class MoveSkill(Component):
    """
    """
    def __init__(self, *args):
        super(MoveSkill, self).__init__()
        self.skills = set(args)
        print('Move is created')

    def __str__(self):
        return super(MoveSkill, self).__str__() + 'MoveSkill: {0}'.format(
            self.skills)


class Image(Component):
    """
    Information about graphical representation.
    """
    def __init__(self, img_name):
        super(Image, self).__init__()
        self.name = img_name
        self.type = None
        print('Image is created')

    def __str__(self):
        return super(Image, self).__str__() + 'Image: name = {0}, type = {1}'.format(
            self.name, self.type)


class Terrain(Component):
    def __init__(self, name):
        super(Terrain, self).__init__()
        self.name = name
        print('Terrain is created')

    def __str__(self):
        return super(Terrain, self).__str__() + 'Terrain: name = {0}'.format(
            self.name)

if __name__ == '__main__':
    print(Position((0, 0, 0)))
    print(Image('wall'))
    print(Terrain('grass'))
    print(MoveSkill('grass', 'water'))


