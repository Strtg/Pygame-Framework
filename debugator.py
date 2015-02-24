from __future__ import print_function


def debugator(f):
    def debug(*args, **kwargs):
        # deb = False
        deb = True
        if deb == True:
            print(f.__name__, 'starting...')
        return f(*args, **kwargs)
    return debug