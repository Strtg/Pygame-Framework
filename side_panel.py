import classes
import render
import layer
import pygame
import utils
import metagame
import escape_screen

alls = []
hoverable = []
clickable = []

limit = 220  # minimap size
factor = 1.0 # if map is to large for minimap
padding = 4 # for side panel elements
width = 190 + 2 * padding  # side panel width

big_map = None
big_camera = None
mini_camera = None
mini_map = None

def setup(_map):
    global big_map, mini_camera, factor, mini_map
    big_map = _map

    background = classes.HUD_Sprite(pygame.Surface((width, render.rect.h)).convert(), render.rect.topright, layer.hud)
    background.rect.move_ip(-width, 0)
    background.image.fill((15, 15, 15))
    alls.append(background)

    exit_button = classes.HUD_Sprite('x-button2-t-', (0, 0), layer.hud + 1, on_click=escape_click)
    alls.append(exit_button)
    hoverable.append(exit_button)
    clickable.append(exit_button)
    exit_button.rect.topright = background.rect.topright
    exit_button.rect.move_ip(-padding, padding)

    min_button = classes.HUD_Sprite('min-button-t-', (background.rect.right - 88, background.rect.top), layer.hud + 1)
    alls.append(min_button)
    hoverable.append(min_button)
    clickable.append(min_button)
    min_button.rect.topright = exit_button.rect.topleft
    min_button.rect.move_ip(-padding, 0)

    next_turn_button = classes.HUD_Sprite('next-turn-button-t-', background.rect.midtop, layer.hud + 1)
    next_turn_button.image = next_turn_button.image.copy()
    next_turn_button.rect.bottomright = background.rect.bottomright
    next_turn_button.rect.move_ip(-padding, -padding)
    new_game_label = utils.label_surface('NEXT TURN', 'TranscendsGames', 20, (80, 120, 80))
    utils.center_blit(next_turn_button.image, new_game_label)
    alls.append(next_turn_button)
    hoverable.append(next_turn_button)
    clickable.append(next_turn_button)

    frame = classes.HUD_Sprite('minimap-t-', (0, 0), layer.hud + 1)
    frame.rect.bottomright = next_turn_button.rect.topright
    frame.rect.move_ip(0, -padding)
    alls.append(frame)
    hoverable.append(frame)
    clickable.append(frame)

    mini_map = classes.HUD_Sprite(pygame.Surface((big_map['map_width'], big_map['map_height'])), (0, 0), layer.hud + 2)
    bigger_side = max(mini_map.rect.size)
    print('rect and bigger side is', mini_map.rect.size, bigger_side)
    factor = 1.0
    if bigger_side > limit:
        factor = 1.0 * limit / bigger_side
        mini_map.image = pygame.Surface((mini_map.rect.w * factor, mini_map.rect.h * factor))
        mini_map.rect = mini_map.image.get_rect()
    mini_map.image.fill((0, 0, 10))
    mini_map.rect.center = frame.rect.center
    alls.append(mini_map)
    hoverable.append(mini_map)
    clickable.append(mini_map)

    print('FACTOR', factor)
    print('MINI-MAP SIZE', mini_map.rect)
    # print('MINICAMERA', minimap.mini_camera)


def show():
    for elem in alls:
        elem.show()

def hide():
    for elem in alls:
        elem.hide()

def escape_click():
    escape_screen.show()
    metagame.stage = 'escape_screen'

def mouse_click(mouse_pos):
    utils.click(mouse_pos, clickable)

def killall():
    global alls, hoverable, clickable
    for elem in alls:
        elem.kill()
    alls = []
    hoverable = []
    clickable = []
