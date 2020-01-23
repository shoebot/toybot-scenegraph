class Path:
    type = "path"

    def __init__(self, coords=None):
        if coords is None:
            self.coords = []
        else:
            self.coords = coords

    def add_point(self, x, y):
        self.coords.append((x, y))

    def __repr__(self):
        return f"<Path: {self.coords}>"
