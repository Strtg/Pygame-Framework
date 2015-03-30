from __future__ import print_function
import random
import const

UNHAPPY_GROWTH = 0.997
GROWTH_IN_BUILDINGS = 1.002


def coord(x_or_y):
    return x_or_y * const.GRID_SIZE


def create_prefix(s):
    if s == 'new0':
        chance = 20
    elif s == 'new1':
        chance = 6
    elif s == 'new2':
        chance = 2
    else:
        return ''
    if random.randint(1, chance) == 1:
        return 'New '
    else:
        return ''

def format_planet_name(s):
    return s.format(new0=create_prefix('new0'), new1=create_prefix('new1'), new2=create_prefix('new2'),
                    number=create_roman_number())

def create_roman_number():
    arab_number = random.randint(1, 13)
    arab_number = random.randint(1, arab_number + 3)
    arab_number = random.randint(1, arab_number + 2)
    arab_number = random.randint(1, arab_number + 2)
    if arab_number == 1: roman_number = 'I'
    elif arab_number == 2: roman_number = 'II'
    elif arab_number == 3: roman_number = 'III'
    elif arab_number == 4: roman_number = 'IV'
    elif arab_number == 5: roman_number = 'V'
    elif arab_number == 6: roman_number = 'VI'
    elif arab_number == 7: roman_number = 'VII'
    elif arab_number == 8: roman_number = 'VIII'
    elif arab_number == 9: roman_number = 'IX'
    elif arab_number == 10: roman_number = 'X'
    elif arab_number == 11: roman_number = 'XI'
    elif arab_number == 12: roman_number = 'XII'
    elif arab_number == 13: roman_number = 'XIII'
    elif arab_number == 14: roman_number = 'XIV'
    else: roman_number = 'III'
    return roman_number


def pop_growth(pop, growth, unrest):
    unrest_pop = pop * unrest
    return (pop - unrest_pop) * growth + unrest_pop * UNHAPPY_GROWTH


def unrest_after_drop_pop(pop_dropped, pop, unrest):
    unhappy_pop = pop * unrest
    happy_pop = pop - unhappy_pop
    unhappy_pop += pop_dropped
    new_unrest = unhappy_pop / (unhappy_pop + happy_pop)
    return new_unrest


class TAX(object):
    class ZERO(object):
        PERCENT = 0.1
        UNREST = -0.004
    class LOW(object):
        PERCENT = 0.6
        UNREST = 0.0
    class MEDIUM(object):
        PERCENT = 1.0
        UNREST = +0.003
    class HIGH(object):
        PERCENT = 1.4
        UNREST = -0.006
    class VERY_HIGH(object):
        PERCENT = 2.0
        UNREST = -0.018


class PLANET(object):
    class EARTH_LIKE(object):
        METAL = 1.0
        SUPPLY = 1.0
        FUEL = 1.0
        GROWTH = 1.003
        BUILDING_COST = 1.0
        PNG = 'earth'
    class DESERT(object):
        METAL = 1.0
        SUPPLY = 0.3
        FUEL = 4.0
        GROWTH = 1.002
        BUILDING_COST = 2.0
        PNG = 'desert'
    class PARADISE(object):
        METAL = 1.0
        SUPPLY = 2.0
        FUEL = 1.0
        GROWTH = 1.004
        BUILDING_COST = 1.0
        PNG = 'paradise'
    class WATER(object):
        METAL = 0.2
        SUPPLY = 0.8
        FUEL = 0.8
        GROWTH = 1.001
        BUILDING_COST = 2.0
        PNG = 'water'
    class VOLCANIC(object):
        METAL = 6.0
        SUPPLY = 0.5
        FUEL = 5.0
        GROWTH = 1.0
        BUILDING_COST = 4.0
        PNG = 'volcano'
    class ICE(object):
        METAL = 1.0
        SUPPLY = 0.5
        FUEL = 0.6
        GROWTH = 1.001
        BUILDING_COST = 2.0
        PNG = 'ice'


if __name__ == '__main__':
    print(create_roman_number())
    print(create_roman_number())
    print(create_roman_number())
    print(create_roman_number())
    print(create_roman_number())
    print(create_roman_number())
    print(create_roman_number())
    print(create_roman_number())
    print(create_roman_number())
    print(create_roman_number())