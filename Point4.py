
import math

class Point: 
    # __new__(), __init__(), __repr__(), __eq__()
    counter=0 # a class attribute or class variable
    
    @staticmethod  # a decorator
    def maxX(): # a class method
        return 1000
        
    def __init__(self, *values): # the constructor
        if len(values) == 2:
            if values[0] < Point.maxX():
                self.x=values[0]
            self.y=values[1]
            Point.counter += 1
        elif len(values) == 0:
            self.x=0
            self.y=0
            Point.counter += 1
        else:
            raise Exception("Wrong number of arguments received!")
            
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x+other.x, self.y+other.y)
        elif isinstance(other, int):
            return Point(self.x+other, self.y+other)
        else:
            print("Wrong kind of arguments received!")
            return self
            # A better strategy will be to raise an Exception !!
            
    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    
    def clear(self):
        self.x=0
        self.y=0
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 

print("Counter", Point.counter)
print("Maximum value a X may take: ",Point.maxX())
p1=Point(1,2) # p1 is an instance of the class Point
print(p1) # <1,2>
p2=p1
print(p2) # <1,2>
p2.x=45
print(p2)
print(p1)
print(id(p1), id(p2))
print("Counter", Point.counter)
p1.clear()
print(p2) # <1,2>
p2.x=100
print(p2)
print(p1)
print(id(p1), id(p2))
p0=Point()
print("Counter", Point.counter)


