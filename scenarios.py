# from __future__ import print_function
import names
import random
import formula
import sys


scenarios = []

scenarios.append({'name': 'The First Scenario',
                  'map_width': 400,
                  'map_height': 400,
                  'human_players': 50,
                  'AI_players': 0,
                  'number_of_planets': 300,
                  'percent_of_nebulas': 20,
                })

scenarios.append({'name': 'The Second Scenario',
                  'map_width': 5,
                  'map_height': 5,
                  'human_players': 2,
                  'AI_players': 2,
                  'number_of_planets': 25,
                  'percent_of_nebulas': 65,
                })

def create_map(scenario):
    map = {}

    return map

def create_players(scenario):
    players = []
    how_many_human_players = scenario['human_players']
    if how_many_human_players > 0:
        for i in range(how_many_human_players):
            players.append('Player ' + str(i + 1))
    how_many_AI_players = scenario['AI_players']
    if how_many_AI_players > 0:
        for i in range(how_many_AI_players):
            players.append('AI ' + str(i + 1))
    return players, len(players)

def create_planet_locations(scenario):
    w_coord = range(scenario['map_width'])
    h_coord = range(scenario['map_height'])
    how_many_planets = scenario['number_of_planets']
    if how_many_planets > len(w_coord) * len(h_coord):
        print 'Error, to many planets for map in the scenario:', '\'' + scenario['name'] + '\''
        sys.exit()
    planets_locations = []
    while len(planets_locations) < how_many_planets:
        location = (random.choice(w_coord), random.choice(h_coord))
        if location in planets_locations:
            continue
        else:
            planets_locations.append(location)
    return planets_locations



def create_planet_name(list1, list2):
    if list2 and not list1:
        name = list2.pop()
    elif list1 and not list2:
        name = list1.pop()
    elif not list1 and not list2:
        name = 'Unnamed Planet'
    elif list1 and list2:
        if random.choice([1, 1, 1, 0, 0]) == 1:
            name = list1.pop()
        else:
            name = list2.pop()
    return formula.format_planet_name(name)









if __name__ == '__main__':
    random.shuffle(names.ice)
    random.shuffle(names.generic)
    random.shuffle(names.earthlike)
    random.shuffle(names.desert)
    random.shuffle(names.paradise)
    random.shuffle(names.volcanic)
    random.shuffle(names.water)
    #
    # for i in range(1):
    #     print(create_planet_name(names.desert, names.generic))
    #
    # print(create_players(scenarios[1]))
    #
    # print()
    print create_planet_locations(scenarios[1])