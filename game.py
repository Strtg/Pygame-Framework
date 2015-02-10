class Game(object):
    def __init__(self, renderer):
        self.is_pause = False
        self.renderer = renderer
        self._init_objects()




    def _init_objects(self):
        pass

    def update(self):
        if self.is_pause:
            self.renderer.set_pause(True)
        else:
            pass