
def make(w):

    def make_keyboard():
        dict_with_options = {}
        dict_with_options.update({
            'fps_limit': 200,
            'resolution': (400, 300),
            'fullscreen': 0,
            'debug': 0,
        })
        return dict_with_options

    def make_options():
        dict_with_options = {}
        dict_with_options.update({
            'K_p': 'pause',
            'K_ESCAPE': 'quit',
            'QUIT': 'quit',
            'K_q': 'quit',
        })
        return dict_with_options

    what = w
    if what == 'keyboard':
        return make_keyboard()
    elif what == 'options':
        return make_options()
    else:
        print 'Errorr in defaults.make().'
