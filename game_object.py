import layers as l


class OManager(object):  # object manager

    def __init__(self):
        self.objects = {}

    def create(self, obj):
        self.objects.update({obj.id: obj})








class Object(object):

    _next_id = 0

    def __init__(self):
        self._id = Object._next_id
        Object._next_id += 1

    @property
    def id(self):
        return self._id


class Visible(Object):

    def __init__(self, l=l.background, app='imageholder' ):
        super(Visible, self).__init__()
        self.layer = l
        self.appearance = app


class Clickable(Visible):

    def __init__(self, on_click):
        super(Clickable, self).__init__()
        self.on_click = on_click
