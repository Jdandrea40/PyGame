import math

class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        print("Vector (" + str(self.x) + ", " + str(self.y) + ")")

    def __add__(self, otherVect):
        return Vector(self.x + otherVect.x, self.y + otherVect.y)

    def __sub__(self, otherVect):
        return Vector(self.x - otherVect.x, self.y - otherVect.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def dot(self, otherVect):
        return ((self.x * otherVect.x) + (self.y * otherVect.y))
    
    def scale(self, scaleFactor):
        return Vector(self.x * scaleFactor, self.y * scaleFactor)

    def length(self):       
        return float(math.sqrt((self.x * self.x) + (self.y * self.y)))

    def normalize(self):
        mag = self.length()
        if mag > 0:
            normalX = self.x / mag
            normalY = self.y / mag
            return Vector(normalX, normalY)
        else:
            return Vector(0, 0)

