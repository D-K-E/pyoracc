class Line(object):
    def __init__(self, label):
        self.label = label
        self.words = []
        self.lemmas = []
        self.translation = None
        self.notes = []
        self.references = []
        self.links = []