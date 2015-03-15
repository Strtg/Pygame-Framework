"""
Game state class
"""


class GameState(object):

    def __init__(self):
        self.minor_vars = {}
        self.name = ''
        self.difficulty = 0

        self.comps = {'sprites': {}, 'positions': {},
                      'terrains': {}, 'move_skills': {},
                      'render_tags': {}}

        self.messgs_to_tag_system = []
        self.messgs_to_render_system = []
