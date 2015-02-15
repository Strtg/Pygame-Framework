import layers as l

class Object(object):

    def __init__(self):
        self.important_data = 'hoo hoo hah!'



class Visible(Object):

    def __init__(self, l=l.background, app='imageholder' ):
        super(Visible, self).__init__()
        self.layer = l
        self.appearance = app