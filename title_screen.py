import classes
import render
import layer
import pygame
import utils
import sys
import metagame


alls = []
hoverable = []
clickable = []


def setup():
    logo = classes.HUD_Sprite(utils.label_surface('ALDEBARAN 5000', 'TranscendsGames', 150, (100, 100, 100)), render.rect.midtop, layer.main_menu, visible=0)
    logo.rect.midtop = render.rect.midtop
    logo.rect.move_ip(0, 50)
    alls.append(logo)

    background = classes.HUD_Sprite(pygame.Surface(render.rect.size), render.rect.topleft, layer.main_menu - 1, visible=0)
    background.image.convert()
    background.image.fill((2, 2, 5))
    alls.append(background)

    new_game_button = classes.HUD_Sprite('green-button-t-', render.rect.midtop, layer.main_menu, visible=0, on_click=new_game_click)
    new_game_button.image = new_game_button.image.copy()
    new_game_button.rect.midtop = logo.rect.midbottom
    new_game_button.rect.move_ip(0, 30)
    new_game_label = utils.label_surface('NEW GAME', 'TranscendsGames', 30, (100, 100, 100))
    utils.center_blit(new_game_button.image, new_game_label)
    alls.append(new_game_button)
    hoverable.append(new_game_button)
    clickable.append(new_game_button)

    continue_button = classes.HUD_Sprite('green-button-t-', render.rect.midtop, layer.main_menu, visible=0)
    continue_button.image = continue_button.image.copy()
    continue_button.rect.midtop = new_game_button.rect.midbottom
    continue_button.rect.move_ip(0, 10)
    options_label = utils.label_surface('CONTINUE', 'TranscendsGames', 30, (100, 100, 100))
    utils.center_blit(continue_button.image, options_label)
    alls.append(continue_button)
    hoverable.append(continue_button)
    clickable.append(continue_button)

    options_button = classes.HUD_Sprite('yellow-button-t-', render.rect.midtop, layer.main_menu, visible=0)
    options_button.image = options_button.image.copy()
    options_button.rect.midtop = continue_button.rect.midbottom
    options_button.rect.move_ip(0, 10)
    options_label = utils.label_surface('OPTIONS', 'TranscendsGames', 30, (100, 100, 100))
    utils.center_blit(options_button.image, options_label)
    alls.append(options_button)
    hoverable.append(options_button)
    clickable.append(options_button)

    quit_button = classes.HUD_Sprite('red-button-t-', render.rect.midtop, layer.main_menu, 0, quit_click)
    quit_button.image = quit_button.image.copy()
    quit_button.rect.midtop = options_button.rect.midbottom
    quit_button.rect.move_ip(0, 10)
    quit_label = utils.label_surface('QUIT', 'TranscendsGames', 30, (100, 100, 100))
    utils.center_blit(quit_button.image, quit_label)
    alls.append(quit_button)
    hoverable.append(quit_button)
    clickable.append(quit_button)


def show():
    for elem in alls:
        # print('title show')
        elem.show()


def hide():
    for elem in alls:
        # print(elem, 'fucking hide')
        elem.hide()


def update():
    pass

def killall():
    global alls, hoverable, clickable
    for elem in alls:
        elem.kill()
    alls = []
    hoverable = []
    clickable = []

def new_game_click():
    metagame.new()
    hide()
    print('NNNNNNNNEEEEEWWWWWWW')
    metagame.stage = 'game'

def quit_click():
    hide()
    pygame.quit()
    sys.exit()

def mouse_click(mouse_pos):
    utils.click(mouse_pos, clickable)