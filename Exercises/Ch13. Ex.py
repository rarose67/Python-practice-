"""1. We can represent a rectangle by knowing three things: the location of its lower left corner, its width, and its height. Create a class definition for a Rectangle class using this idea. For instance, to create a Rectangle object at location (4,5) with width 6 and height 5, we would do the following:

loc = Point(4, 5)
r = Rectangle(loc, 6, 5)"""
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

class Rectangle:
    
    def __init__(self, init_llc, init_width, init_height):
        self.corner = init_llc
        self.width = init_width
        self.height = init_height
        
    def is_square(self):
        return (self.height == self.width)
    
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    
    def is_smaller(self, r2):
        return(self.area() < r2.area())
    
    def __repr__(self):
        return "This rectangle has width of {0},and a height of {1}.".format(self.width, self.height)
    
loc = Point(4, 5)
r = Rectangle(loc, 6, 5)

print(r)
print(r.area())

#2. Add the following accessor methods to the Rectangle class: get_width and get_height.
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

class Rectangle:
    
    def __init__(self, init_llc, init_width, init_height):
        self.corner = init_llc
        self.width = init_width
        self.height = init_height
        
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
    
    def is_square(self):
        return (self.height == self.width)
    
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    
    def is_smaller(self, r2):
        return(self.area() < r2.area())
    
    def __repr__(self):
        return "This rectangle has width of {0},and a height of {1}.".format(self.width, self.height)
    
loc = Point(4, 5)
r = Rectangle(loc, 6, 5)

print(r)
print(r.area())

"""3. Add a method area to the Rectangle class that returns the area of any instance:

r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.area(), 50)
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
    
class Rectangle:
    
    def __init__(self, init_llc, init_width, init_height):
        self.corner = init_llc
        self.width = init_width
        self.height = init_height
        
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
    
    def is_square(self):
        return (self.height == self.width)
    
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    
    def is_smaller(self, r2):
        return(self.area() < r2.area())
    
    def __repr__(self):
        return "This rectangle has width of {0},and a height of {1}.".format(self.width, self.height)

from test import testEqual
r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.area(), 50)

"""4. Write a perimeter method in the Rectangle class so that we can find the perimeter of any rectangle instance:

r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.perimeter(), 30)
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
    
class Rectangle:
    
    def __init__(self, init_llc, init_width, init_height):
        self.corner = init_llc
        self.width = init_width
        self.height = init_height
        
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
    
    def is_square(self):
        return (self.height == self.width)
    
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    
    def is_smaller(self, r2):
        return(self.area() < r2.area())
    
    def __repr__(self):
        return "This rectangle has width of {0},and a height of {1}.".format(self.width, self.height)

from test import testEqual
r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.perimeter(), 30)

"""5. Write a transpose method in the Rectangle class that swaps the width and the height of any rectangle instance:

r = Rectangle(Point(100, 50), 10, 5)
testEqual(r.width, 10)
testEqual(r.height, 5)
r.transpose()
testEqual(r.width, 5)
testEqual(r.height, 10)
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
    
class Rectangle:
    
    def __init__(self, init_llc, init_width, init_height):
        self.corner = init_llc
        self.width = init_width
        self.height = init_height
        
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
    
    def is_square(self):
        return (self.height == self.width)
    
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    
    def is_smaller(self, r2):
        return(self.area() < r2.area())
    
    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp
    
    def __repr__(self):
        return "This rectangle has width of {0},and a height of {1}.".format(self.width, self.height)

from test import testEqual
r = Rectangle(Point(100, 50), 10, 5)
testEqual(r.width, 10)
testEqual(r.height, 5)
r.transpose()
testEqual(r.width, 5)
testEqual(r.height, 10)

"""6. Write a new method called contains in the Rectangle class to test if a Point falls within the rectangle. For this exercise, assume that a rectangle at (0,0) with width 10 and height 5 has open upper bounds on the width and height, i.e. it stretches in the x direction from [0 to 10), where 0 is included but 10 is excluded, and from [0 to 5) in the y direction. So it does not contain the point (10, 2). These tests should pass:

r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.contains(Point(0, 0)), True)
testEqual(r.contains(Point(3, 3)), True)
testEqual(r.contains(Point(3, 7)), False)
testEqual(r.contains(Point(3, 5)), False)
testEqual(r.contains(Point(3, 4.99999)), True)
testEqual(r.contains(Point(-3, -3)), False)
"""
from test import testEqual

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
    
class Rectangle:
    
    def __init__(self, init_llc, init_width, init_height):
        self.corner = init_llc
        self.width = init_width
        self.height = init_height
        
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
    
    def is_square(self):
        return (self.height == self.width)
    
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    
    def is_smaller(self, r2):
        return(self.area() < r2.area())
    
    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp
        
    def contains(self, point):
        left_bound = self.corner.get_x()
        lower_bound = self.corner.get_y()
        right_bound = left_bound + self.width
        upper_bound = lower_bound + self.height
        px = point.get_x()
        py = point.get_y()
        
        if((px >= left_bound) and (px < right_bound) and (py >= lower_bound) and (py < upper_bound)):
            return True
        else:
            return False
    
    def __repr__(self):
        return "This rectangle has width of {0},and a height of {1}.".format(self.width, self.height)


r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.contains(Point(0, 0)), True)
testEqual(r.contains(Point(3, 3)), True)
testEqual(r.contains(Point(3, 7)), False)
testEqual(r.contains(Point(3, 5)), False)
testEqual(r.contains(Point(3, 4.99999)), True)
testEqual(r.contains(Point(-3, -3)), False)

#7. Write a new method called diagonal that will return the length of the diagonal that runs from the lower left corner to the opposite corner.
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
    
class Rectangle:
    
    def __init__(self, init_llc, init_width, init_height):
        self.corner = init_llc
        self.width = init_width
        self.height = init_height
        
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
    
    def is_square(self):
        return (self.height == self.width)
    
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    
    def is_smaller(self, r2):
        return(self.area() < r2.area())
    
    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp
        
    def contains(self, point):
        left_bound = self.corner.get_x()
        lower_bound = self.corner.get_y()
        right_bound = left_bound + self.width
        upper_bound = lower_bound + self.height
        px = point.get_x()
        py = point.get_y()
        
        if((px >= left_bound) and (px < right_bound) and (py >= lower_bound) and (py < upper_bound)):
            return True
        else:
            return False
    
    def diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5
    
    def __repr__(self):
        return "This rectangle has width of {0},and a height of {1}.".format(self.width, self.height)



from test import testEqual
r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.diagonal(), 11.1803398875)

r1 = Rectangle(Point(0,0), 12, 4)
testEqual(r1.diagonal(), 12.6491106407)

r2 = Rectangle(Point(0,0), 1,2)
testEqual(r2.diagonal(), 2.2360679775)

"""8. There are some games where we put a rectangular “bounding box” around our sprites in the game. We can then do collision detection between, say, bombs and spaceships, by comparing whether their rectangles overlap anywhere.

Write a function to determine whether two rectangles collide. Hint: this might be quite a tough exercise! Think carefully about all the cases as you code."""
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
    
class Rectangle:
    
    def __init__(self, init_llc, init_width, init_height):
        self.corner = init_llc
        self.width = init_width
        self.height = init_height
        
    def get_corner(self):
        return self.corner
    
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
    
    def is_square(self):
        return (self.height == self.width)
    
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    
    def is_smaller(self, r2):
        return(self.area() < r2.area())
    
    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp
        
    def contains(self, point):
        left_bound = self.corner.get_x()
        lower_bound = self.corner.get_y()
        right_bound = left_bound + self.width
        upper_bound = lower_bound + self.height
        px = point.get_x()
        py = point.get_y()
        
        if((px >= left_bound) and (px < right_bound) and (py >= lower_bound) and (py < upper_bound)):
            return True
        else:
            return False
    
    def collide(self, r2):
        corner = r2.get_corner()
        cx = corner.get_x()
        cy = corner.get_y()
        w2 = r2.get_width()
        h2 = r2.get_height()
        x = 0
        does_collide = False
        
        while ((does_collide == False) and (x < w2)):
            y = 0
            while ((does_collide == False) and (y < h2)):
                p1 = Point(cx + x, cy +y)
                does_collide = self.contains(p1)
                y += 1
            x += 1
        
        return does_collide
         
    def diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5
    
    def __repr__(self):
        return "This rectangle has width of {0},and a height of {1}.".format(self.width, self.height)

r = Rectangle(Point(0, 0), 10, 5)
r1 = Rectangle(Point(0,0), 12, 4)
r2 = Rectangle(Point(0,0), 1,2)

print(r1.collide(r2))


"""Weekly Graded Assignment

The code below contains a Chatbot class. A Chatbot is an object that can engage in rudimentary conversation with a human. You will be asked to define a subclass that inherits from this Chatbot superclass.

Your job is to make a subclass called BoredChatbot that inherits from Chatbot, but acts a little differently, in the following way:

    A bored chatbot has a short attention span. When the human says something that is longer than 20 characters, it should respond by saying:

        “zzz... Oh excuse me, I dozed off reading your essay.”

    If, on the other hand, the human says something with a length of 20 characters or less, then the bored chatbot should respond just like a normal chatbot would.

Note that we are requiring you to use inheritance. Your new BoredChatbot class must be a subclass of the Chatbot class, and your subclass should only implement the things that make it distinct. (See the Inheritance chapter for a review of how this works.)
"""

class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"


# TODO define a class called BoredChatbot
class BoredChatbot(Chatbot):
    """ A chatbot that has a short attention span. """
    
    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said.  
        If the person provides a long response, return a sarcastic response."""
        
        if len(prompt_from_human) > 20:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            return "It is very interesting that you say: '" + prompt_from_human + "'"
    
def main():
    # make a chatbot
    sally = BoredChatbot("Sally")
    # introduce the chatbot and allow the user to say something
    human_message = input(sally.greeting())
    # respond to the user
    print(sally.response(human_message))
    
    # make a chatbot
    jim = Chatbot("Jim")
    # introduce the chatbot and allow the user to say something
    human_message2 = input(jim.greeting())
    # respond to the user
    print(jim.response(human_message2))

if __name__ == "__main__":
    main()