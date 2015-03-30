import render
import config
import pygame
import side_panel
import metagame
import const
import classes
import layer
import game_state
rect = pygame.Rect(0, 0, 0, 0)
loc_top_left = (0, 0)
loc_bottom_right = (0, 0)
old_top_left = (0, 0)
old_bottom_right = (0, 0)
mini_camera = pygame.Rect(0, 0, 0, 0)
diff_x = 0
diff_y = 0

rect_to_hold_on = pygame.Rect(0, 0, 0, 0)
margin = 2000
left_max = -2000
right_max = 4000
top_max = 2000
bottom_max = 2000

is_moving_left = 0
is_moving_right = 0
is_moving_up = 0
is_moving_down = 0
is_moved = 1

def setup():
    global rect, rect_to_hold_on, mini_camera
    rect = pygame.Rect(render.rect.x, render.rect.y, render.rect.w - side_panel.width, render.rect.h)
    rect.topleft = (300, 300)
    update_locs()
    mini_camera = pygame.Rect(0, 0, rect.w / const.GRID_SIZE * side_panel.factor, rect.h / const.GRID_SIZE * side_panel.factor)

    side_panel.mini_camera = classes.HUD_Sprite(pygame.Surface(mini_camera.size), (0, 0), layer.hud + 3)
    side_panel.alls.append(side_panel.mini_camera)
    side_panel.hoverable.append(side_panel.mini_camera)
    side_panel.clickable.append(side_panel.mini_camera)
    pygame.draw.rect(side_panel.mini_camera.image, (100, 100, 100), mini_camera, 1)
    side_panel.mini_camera.image.set_colorkey((0, 0, 0))
    side_panel.mini_camera.show()
    side_panel.mini_camera.rect.topleft = side_panel.mini_map.rect.x + loc_top_left[0] * side_panel.factor, side_panel.mini_map.rect.y + loc_top_left[1] * side_panel.factor

    print('MINICAMERA', mini_camera)
    print('CAMERA', loc_top_left, loc_bottom_right)

    add_to_container_on_start()

    rect_to_hold_on = render.rect
    # for candy in metagame.current_game_state.eye_candies:
    #     pass


def hold_on(rect):
    global rect_to_hold_on
    rect_to_hold_on = rect


def update():
    global rect, is_moved
    is_moved = 0
    if is_moving_left == 1:
        rect.move_ip(-config.config_dict['camera_speed'], 0)
        is_moved = 1
    if is_moving_right == 1:
        rect.move_ip(config.config_dict['camera_speed'], 0)
        is_moved = 1
    if is_moving_up == 1:
        rect.move_ip(0, -config.config_dict['camera_speed'])
        is_moved = 1
    if is_moving_down == 1:
        rect.move_ip(0, config.config_dict['camera_speed'])
        is_moved = 1

    if is_moved == 1:
        # print('IS MOVED')
        update_locs()
        remove_from_container()
        add_to_container()
        side_panel.mini_camera.rect.topleft = side_panel.mini_map.rect.x + loc_top_left[0] * side_panel.factor, side_panel.mini_map.rect.y + loc_top_left[1] * side_panel.factor
        # print(side_panel.mini_camera.rect.topleft)
        side_panel.mini_camera.dirty = 1

def update_locs():
    global loc_top_left, loc_bottom_right, old_top_left, old_bottom_right, diff_x, diff_y
    old_top_left = loc_top_left
    old_bottom_right = loc_bottom_right
    loc_top_left = rect.x / const.GRID_SIZE, rect.y / const.GRID_SIZE
    loc_bottom_right = rect.right / const.GRID_SIZE, rect.bottom / const.GRID_SIZE
    diff_x = loc_top_left[0] - old_top_left[0]
    diff_y = loc_top_left[1] - old_top_left[1]
    # if old_top_left != loc_top_left:
        # print loc_top_left, old_top_left
        # print diff_x, diff_y

def add_to_container_on_start():

    for _y in range(loc_top_left[1]-1, loc_bottom_right[1] + 2):
        for _x in range(loc_top_left[0] - 1, loc_bottom_right[0] + 2):
            try:
                for space in game_state.locations[(_x, _y)].spaces:
                    space.add(render.renderable_container)
                    render.renderable_container.change_layer(space, space.layer)
                for nebula in game_state.locations[(_x, _y)].nebulas:
                    nebula.add(render.renderable_container)
                    render.renderable_container.change_layer(nebula, nebula.layer)
                for grid in game_state.locations[(_x, _y)].grids:
                    grid.add(render.renderable_container)
                    render.renderable_container.change_layer(grid, grid.layer)
                for planet in game_state.locations[(_x, _y)].planets:
                    planet.sprite.add(render.renderable_container)
                    render.renderable_container.change_layer(planet.sprite, planet.sprite.layer)
            except KeyError:
                pass
                # print('out of map')

def append_to_locs(top_left, bottom_right, locs_to_add):
    for _y in range(top_left[1], bottom_right[1]):
        for _x in range(top_left[0], bottom_right[0]):
            locs_to_add.append((_x, _y))
            # print 'add', _x, _y

def add_to_container():
    locs_to_add = []
    counter = [0]

    if diff_x == 0 and diff_y == 0:
        return

    if diff_x > 0:  # to right
        to_cut_top_left = loc_bottom_right[0] - diff_x, loc_top_left[1] - 3
        to_cut_bottom_right = loc_bottom_right[0] + 2, loc_bottom_right[1] + 1
        append_to_locs(to_cut_top_left, to_cut_bottom_right, locs_to_add)

    elif diff_x < 0:
        to_cut_top_left = loc_top_left[0] - 3, loc_top_left[1] - 3
        to_cut_bottom_right = loc_top_left[0] - 1 - diff_x, loc_bottom_right[1] + 3
        append_to_locs(to_cut_top_left, to_cut_bottom_right, locs_to_add)

    if diff_y > 0:
        to_cut_top_left = loc_top_left[0] - 3, loc_bottom_right[1] - diff_y
        to_cut_bottom_right = loc_bottom_right[0] + 1, loc_bottom_right[1] + 2
        append_to_locs(to_cut_top_left, to_cut_bottom_right, locs_to_add)

    elif diff_y < 0:
        to_cut_top_left = loc_top_left[0] - 3, loc_top_left[1] - 3
        to_cut_bottom_right = loc_bottom_right[0] + 3, loc_top_left[1] - diff_y
        append_to_locs(to_cut_top_left, to_cut_bottom_right, locs_to_add)


    for loc in locs_to_add:
        # print counter
        try:
            for space in game_state.locations[loc].spaces:
                space.add(render.renderable_container)
                render.renderable_container.change_layer(space, space.layer)
            for nebula in game_state.locations[loc].nebulas:
                nebula.add(render.renderable_container)
                render.renderable_container.change_layer(nebula, nebula.layer)
                # print 'add space', _x, _y
            for grid in game_state.locations[loc].grids:
                grid.add(render.renderable_container)
                render.renderable_container.change_layer(grid, grid.layer)
            for planet in game_state.locations[loc].planets:
                planet.sprite.add(render.renderable_container)
                render.renderable_container.change_layer(planet.sprite, planet.sprite.layer)
                # print 'add planet', _x, _y
        except KeyError:
            pass
            # print('out of map')



def remove_from_container():
    locs_to_remove = []

    if diff_x == 0 and diff_y == 0:
        return
    if diff_x < 0:  # to left
        to_cut_top_left = loc_bottom_right[0] + 2, loc_top_left[1] - 4
        to_cut_bottom_right = loc_bottom_right[0] + 4 - diff_x, loc_bottom_right[1] +4
        append_to_locs(to_cut_top_left, to_cut_bottom_right, locs_to_remove)
    elif diff_x > 0:
        to_cut_top_left = loc_top_left[0] - 5 - diff_x, loc_top_left[1] - 4
        to_cut_bottom_right = loc_top_left[0] - 4, loc_bottom_right[1] + 4
        append_to_locs(to_cut_top_left, to_cut_bottom_right, locs_to_remove)
    if diff_y < 0:
        to_cut_top_left = loc_top_left[0] - 4, loc_bottom_right[1] + 2
        to_cut_bottom_right = loc_bottom_right[0] + 4, loc_bottom_right[1] + 4 - diff_y
        append_to_locs(to_cut_top_left, to_cut_bottom_right, locs_to_remove)
    elif diff_y > 0:
        to_cut_top_left = loc_top_left[0] - 4, loc_top_left[1] - 5 - diff_y
        to_cut_bottom_right = loc_bottom_right[0] + 4, loc_top_left[1] - 4
        append_to_locs(to_cut_top_left, to_cut_bottom_right, locs_to_remove)

    for loc in locs_to_remove:
        try:
            for space in game_state.locations[loc].spaces:
                space.kill()
            for nebula in game_state.locations[loc].nebulas:
                render.renderable_container.remove(nebula)
            for grid in game_state.locations[loc].grids:
                render.renderable_container.remove(grid)
            for planet in game_state.locations[loc].planets:
                planet.sprite.kill()
                # print 'remove planet', _x, _y
        except KeyError:
            pass
            # print('out of map')
