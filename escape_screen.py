import classes
import render
import layer
import pygame
import utils
import title_screen
import metagame
import game_state

alls = []
hoverable = []
clickable = []

padding = 30


def setup():
    resume_game_button = classes.HUD_Sprite('green-button-t-', render.rect.midtop, layer.main_menu, visible=0, on_click=resume_click)
    resume_game_button.image = resume_game_button.image.copy()
    new_game_label = utils.label_surface('RESUME', 'TranscendsGames', 30, (100, 100, 100))
    utils.center_blit(resume_game_button.image, new_game_label)
    del new_game_label
    alls.append(resume_game_button)
    hoverable.append(resume_game_button)
    clickable.append(resume_game_button)

    options_button = classes.HUD_Sprite('yellow-button-t-', render.rect.midtop, layer.main_menu, visible=0)
    options_button.image = options_button.image.copy()
    options_label = utils.label_surface('OPTIONS', 'TranscendsGames', 30, (100, 100, 100))
    utils.center_blit(options_button.image, options_label)
    alls.append(options_button)
    hoverable.append(options_button)
    clickable.append(options_button)

    quit_button = classes.HUD_Sprite('red-button-t-', render.rect.midtop, layer.main_menu, visible=0, on_click=quit_click)
    quit_button.image = quit_button.image.copy()
    quit_label = utils.label_surface('SAVE & QUIT', 'TranscendsGames', 30, (100, 100, 100))
    utils.center_blit(quit_button.image, quit_label)
    alls.append(quit_button)
    hoverable.append(quit_button)
    clickable.append(quit_button)

    background = classes.HUD_Sprite(pygame.Surface((quit_button.rect.w + (padding * 2), quit_button.rect.h * 3 + (padding * 4))), render.rect.topleft, layer.main_menu - 1, visible=0)
    background.image.fill((2, 2, 2))
    border = 5
    pygame.draw.rect(background.image, (100, 100, 100), (background.rect.x, background.rect.y, background.rect.w, background.rect.y + border))
    pygame.draw.rect(background.image, (100, 100, 100), (background.rect.x, background.rect.h - border, background.rect.w, background.rect.h))
    pygame.draw.rect(background.image, (100, 100, 100), (background.rect.x, background.rect.y, background.rect.x + border, background.rect.h))
    pygame.draw.rect(background.image, (100, 100, 100), (background.rect.w - border, background.rect.y, background.rect.w, background.rect.h))
    background.image.set_colorkey((0, 0, 0), pygame.RLEACCEL)
    background.rect.center = render.rect.center
    for y in range(render.rect.h):
        if y % 4 == 0:
            pygame.draw.line(background.image, (0, 0, 0), (0, y), (background.rect.w, y), 1)
    alls.append(background)

    resume_game_button.rect.midtop = background.rect.midtop
    resume_game_button.rect.move_ip(0, padding)

    options_button.rect.midtop = resume_game_button.rect.midbottom
    options_button.rect.move_ip(0, (padding))
    quit_button.rect.midtop = options_button.rect.midbottom
    quit_button.rect.move_ip(0, (padding))


def show():
    for elem in alls:
        elem.show()


def hide():
    for elem in alls:
        elem.hide()

def killall():
    global alls, hoverable, clickable
    for elem in alls:
        elem.kill()
    alls = []
    hoverable = []
    clickable = []


def update():
    pass

def resume_click():

    print('RREESSUUMMEE')
    hide()
    metagame.stage = 'game'


def quit_click():
    hide()
    metagame.stage = 'title_screen'
    title_screen.show()
    game_state.delete()




def mouse_click(mouse_pos):
    utils.click(mouse_pos, clickable)
