class Rect(object):
    "A simple rect object for building rooms, constructing trigger areas, etc."
    def __init__(self, x, y, width, height):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height
        self.width = width
        self.height = height
    def center(self):
        xCenter = (self.x1 + self.x2) / 2
        yCenter = (self.y1 + self.y2) / 2
        return (xCenter, yCenter)
    def intersect(self, other):
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)
