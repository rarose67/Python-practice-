#1. Add a distance_from_point method that works similar to distance_from_origin except that it takes a Point as a parameter and computes the distance between that point and self.
class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distance_from_point(self, p2):
        return (((self.x - p2.x) ** 2) + ((self.y - p2.y) ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
p = Point(3, 4)
q = Point(5, 12)
dist = p.distance_from_point(q)

print(dist)

#2. Add a method reflect_x to the class Point which returns a new Point, one which is the reflection of the point across the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)
class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def reflect_x(self):
        return Point(-(self.x), self.y)

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
p = Point(3, 5)
q = p.reflect_x()
print(q)

"""3. Add a method slope_from_origin, which returns the slope of the line joining the origin to the point. For example,

>>> Point(4, 10).slope_from_origin()
2.5
>>> Point(12, -3).slope_from_origin()
-0.25
>>> Point(-6, 0).slope_from_origin()
0

The equation for calculating slope between any two points is slope = (Y2 - Y1) / (X2 - X1). Remember that dividing by 0 is not allowed, so there are some inputs that will cause your method to fail. Return None when that happens.
"""
class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    # TODO define a method called slope_from_origin here
    def slope_from_origin(self):
        if self.x != 0:
            return (self.y / self.x)


# some tests to check your code
from test import testEqual
testEqual( Point(4, 10).slope_from_origin(), 2.5 )
testEqual( Point(5, 10).slope_from_origin(), 2 )
testEqual( Point(0, 10).slope_from_origin(), None )
testEqual( Point(20, 10).slope_from_origin(), 0.5 )
testEqual( Point(20, 20).slope_from_origin(), 1 )
testEqual( Point(4, -10).slope_from_origin(), -2.5 )
testEqual( Point(-4, -10).slope_from_origin(), 2.5 )
testEqual( Point(-6, 0).slope_from_origin(), 0 )

#4. Add a method called move that will take two parameters, call them dx and dy. The method will cause the point to move in the x and y direction the number of units given. (Hint: you will change the values of the state of the point)
class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
p = Point(3, 4)
print(p)
p.move(3, 4)
print(p)
p.move(-1, -2)
print(p)


"""Weekly Graded Assignment

Create a Car class that has the following characteristics:

    It has a gas_level attribute.
    It has a constructor (__init__ method) that takes a float representing the initial gas level and sets the gas level of the car to this value.
    It has an add_gas method that takes a single float value and adds this amount to the current value of the gas_level attribute.
    It has a fill_up method that sets the car’s gas level up to 13.0 by adding the amount of gas necessary to reach this level. It will return a float of the amount of gas that had to be added to the car to get the gas level up to 13.0. However, if the car’s gas level was greater than or equal to 13.0 to begin with, then it doesn’t need to add anything and it simply returns a 0.

(Note: you can call the add_gas method from within the fill_up method by using this syntax: self.add_gas(amount).)

Here’s an example.

example_car = Car(9)
print(example_car.fill_up())  # should print 4

another_car = Car(18)
print(another_car.fill_up()) # should print 0

Reminder: Don’t forget about the self parameter!
"""

# TODO: add the Car class
class Car:
    
    def __init__(self, init_gas_level):
        """creates a car object with a given gas level"""
        
        self.gas_level = float(init_gas_level)
  
    def add_gas(self, gas):
        self.gas_level += gas
        
    def fill_up(self):
        if(self.gas_level >= 13.0):
            return 0
        else:
            gas_needed = 13.0 - self.gas_level
            self.add_gas(gas_needed)
            return (gas_needed)

example_car = Car(9)
print(example_car.fill_up())  # should print 4

another_car = Car(18)
print(another_car.fill_up()) # should print 0

# some tests to check your code, Do Not Post These in Vocareum
from test import testEqual
testEqual( Car(10).fill_up(), 3 )
testEqual( Car(20).fill_up(), 0 )
testEqual( Car(5.5).fill_up(), 7.5 )
testEqual( Car(12.5).fill_up(), 0.5 )
testEqual( Car(13).fill_up(), 0 )
