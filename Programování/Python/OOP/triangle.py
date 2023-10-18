import os
import math

clear = lambda: os.system('cls')

class Point:
    
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def setCoords(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getCoords(self):
        return (self.getX(), self.getY())

    def __str__(self):
        return f"[{self.getX()},{self.getY()}]"
    
class LineSegment:

    def __init__(self, u=0, v=0, x=0, y=0):
        self.__a = Point(u, v) # vytvoření instance třídy Point
        self.__b = Point(x, y) # vytvoření instance třídy Point
    
    def setLineSegmentCoords(self, u, v, x, y):
        self.__a.setCoords(u, v)
        self.__b.setCoords(x, y)

    def __str__(self):
        return  f"[{self.__a.getX()},{self.__a.getY()}][{self.__b.getX()},{self.__b.getY()}]"

    def getLineSegmentLength(self):
        return math.sqrt(math.pow(self.__a.getX() - self.__b.getX(), 2) + math.pow(self.__a.getY() - self.__b.getY(), 2))
    
class Triangle:

    def __init__(self, a1=0, a2=0, b1=0, b2=0, c1=0, c2=0):
        self.__a = Point(a1, a2)
        self.__b = Point(b1, b2)
        self.__c = Point(c1, c2)

    # c2 = a2 + b2
    def __calculate(ax, ay, bx, by):
        cross = (ax, by)
        return 0

    
    def setTriangleCoords(self, a1, a2, b1, b2, c1, c2):
        self.__a.setCoords(a1, a2)
        self.__b.setCoords(b1, b2)
        self.__c.setCoords(c1, c2)
    
    def __str__(self):
         return  f"[{self.__a.getX()},{self.__a.getY()}]" + f"[{self.__b.getX()},{self.__b.getY()}]" + f"[{self.__c.getX()},{self.__b.getY()}]"

    def getTriangleLength(self): # obvod trojůhelníka
        a_obvod = 0 #pythagorova c+B


clear()

B = Point() # vytvoření bodu B jako instance třídy Point
B.setCoords(1, -2) # nastavení souřadnic bodu B 
print(B) # volání magické metody __str__ objektu B

U = LineSegment(1, 3, 4, -1)
U.setLineSegmentCoords(1, 3, 4, 0)
print(U)
print(f"{U.getLineSegmentLength():.2f}")

Trinagle = Triangle(1,2,4,5)
     