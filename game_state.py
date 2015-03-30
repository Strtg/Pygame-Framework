import datetime
import scenarios
import classes
import names
import random
import layer
import render
import formula
import const
import camera
import utils
import side_panel

"""
Game state class
"""

scenario = None
minor_vars = {}
map = None
name = ''
date_of_creating = None
difficulty = None
locations = {}
grid = None
grids = []
map_bg = None
planets = []
eye_candies = []
planet_locations = None
nebulas = []

def setup(nam, diff, scen):
    global scenario, minor_vars, map, name, date_of_creating, difficulty, locations, grid, map_bg, planets, eye_candies, nebulas, grids
    scenario = scen
    minor_vars = {}
    map = None
    name = nam
    date_of_creating = datetime.datetime.now()
    difficulty = diff
    locations = {}
    # grid = classes.Grid(scenarios.scenarios[0]['map_width'], scenarios.scenarios[0]['map_height'], 1, (23, 43, 54))
    # map_bg = classes.MapBackground(scenarios.scenarios[0]['map_width'], scenarios.scenarios[0]['map_height'],(23, 23, 31))
    planets = []
    eye_candies = []
    nebulas = []
    grid_image = utils.make_grid_image(1, (12,23,12))

    for x in range(scenario['map_width']):
        for y in range(scenario['map_height']):
            locations.update({(x, y): classes.Location(x, y, scenario['map_width'] - 1, scenario['map_height'] - 1)})

    for x in range(scenario['map_width']):
        for y in range(scenario['map_height']):
            if random.randint(0, 100) < scenario['percent_of_nebulas']:
                img_name = 'nebula{0:2d}-t-'.format(random.randint(1, const.NEBULAS_PNGS))
                img_name = img_name.replace(' ', '0')
                _x, _y = x, y

                locations[(_x, _y)].nebulas.append(classes.OnMapSprite(img_name, (_x, _y), layer.nebulas, offset=(-5, -5)))
                nebulas.append((_x, _y))

            # else:
            if (x % 4 == 0) and (y % 4 == 0):
                img_name = 'space{0:2d}'.format(random.randint(1, const.SPACE_PNGS))
                img_name = img_name.replace(' ', '0')
                _x, _y = x, y

                locations[(_x, _y)].spaces.append(classes.OnMapSprite(img_name, (_x, _y), layer.cosmos+1))
                eye_candies.append((_x, _y))
                print('spaces:', _x, _y)

                locations[(_x, _y)].grids.append(classes.OnMapSprite(grid_image, (_x, _y), layer.grid))
                grids.append((_x, _y))


    planet_locations = scenarios.create_planet_locations(scenario)

    for location in planet_locations:
        category = random.choice([0, 1, 2, 3, 4])
        if category == 0:
            c = 'earth-like', names.earthlike
        elif category == 2:
            c = 'water', names.water
        elif category == 3:
            c = 'paradise', names.paradise
        elif category == 1:
            c = 'desert', names.desert
        elif category == 4:
            c = 'ice', names.ice
        locations[location].planets.append(classes.Planet(location, c[0], scenarios.create_planet_name(c[1], names.generic)))

        planets.append(location)
        print 'lokacja planety', locations[planets[-1]].planets[-1].location, 'rect', locations[planets[-1]].planets[-1].sprite.start_rect

    side_panel.setup(scenario)

def nebulize():
    global nebulas
    print nebulas

    for location in locations:
        neighbours = 0
        if locations[location].nebulas:
            print location, 'nebula'
            try:
                if locations[(location[0]-1, location[1])].nebulas:
                    neighbours +=1
            except KeyError:
                pass
            try:
                if locations[(location[0]+1, location[1])].nebulas:
                    neighbours +=1
            except KeyError:
                pass
            try:
                if locations[(location[0], location[1]-1)].nebulas:
                    neighbours +=1
            except KeyError:
                pass
            try:
                if locations[(location[0], location[1]+1)].nebulas:
                    neighbours +=1
            except KeyError:
                pass

            print neighbours
            if neighbours <= 1:
                kill_nebula(location)


        else:
            print location, 'not'



def delete():
    global locations, grid, map_bg, planets, eye_candies, planet_locations, nebulas
    print('start deleting')
    kill_sprites()
    locations = {}
    grid.kill()
    grid = None
    map_bg.kill()
    map_bg = None
    planets = []
    eye_candies = []
    nebulas = []
    planet_locations = None

#
def mouse_click(mouse_pos):
    if 1: # if sidepanel
        side_panel.mouse_click(mouse_pos)

def update():
    camera.update()

def kill_sprites():
    for planet in planets:
        for i in locations[planet].planets:
            i.sprite.kill()
    for space in eye_candies:
        for s in locations[space].spaces:
            s.kill()
    for nebula_loc in nebulas:
        kill_nebula(nebula_loc)
    side_panel.killall()




def kill_nebula(location):
    for sprite in locations[location].nebulas:
        sprite.kill()
        print 'NEBULAS TO REMOVE', locations[location].nebulas, sprite
        locations[location].nebulas.remove(sprite)

        print 'NEBULAS AFTER REMOVE', locations[location].nebulas, sprite

    nebulas.remove(location)
