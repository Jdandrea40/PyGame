import math

class Vector(object):

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("Vector (", str(self.x), ", ", str(self.y), ")")

    def __add__(self, otherVect):
        return Vector(self.x + otherVect.x, self.y + otherVect.y)

    def __subtract__(self, otherVect):
        return Vector(self.x - otherVect.x, self.y - otherVect.y)

    def dot(self, otherVect):
        return ((self.x * otherVect.x) + (self.y * otherVect.y))
    
    def scale(self, scaleFactor):
        return Vector(self.x * scaleFactor, self.y * scaleFactor)

    def length(self):       
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def normalize(self, other):
        mag = self.length()
        if mag > 0:
            normalX = self.x / mag
            normalY = self.y / mag
            return Vector(normalX, normalY)
        else:
            print ("WRONG")

