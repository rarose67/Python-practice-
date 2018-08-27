"""1. Use the draw_square function we wrote in this chapter to draw the image shown below. Assume each side is 20 units.

(Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)"""
import turtle

def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("hotpink")
    alex.pensize(5)
    
    alex.up()
    alex.goto(-100, 0)
    alex.down()
    
    for i in range(5):
        draw_square(alex,20)
        alex.up()
        alex.forward(40)
        alex.down()

    wn.exitonclick()

if __name__ == "__main__":
    main()

"""2. Write a program to draw this. Assume the innermost square is 20 units per side and each successive square is 20 units bigger, per side, than the one inside it."""
import turtle

def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("hotpink")
    
    size = 20
    x = 0
    y = 0
    
    for i in range(5):
        draw_square(alex, size)
        
        x = x - 10
        y = y - 10
        size = size + 20
        alex.up()
        alex.goto(x, y)
        alex.down()
        
    wn.exitonclick()
    
if __name__ == "__main__":
    main()

"""3. Write a non-fruitful function draw_poly(t, sides, side_length) which makes a turtle draw a regular polygon. When called with draw_poly(tess, 8, 50)"""
import turtle

def draw_poly(t, sides, side_length):
    """Get turtle t to draw a polygon with sides sides that are side_length long"""

    for i in range(sides):
        t.forward(side_length)
        t.left(360/sides)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("hotpink")
    tess.pensize(3)
    
    draw_poly(tess, 8, 50)
    
    wn.exitonclick()
    
if __name__ == "__main__":
    main()

"""4. The two spirals in this picture differ only by the turn angle. Draw both.

Note: Because this program might receive a TimeLimitError we’ve added some code to our answer to make the turtle go faster (use its speed method) and to increase the time the program is allowed to run to 35 seconds. You can do the latter in your code using:

import sys
sys.setExecutionLimit(35000)
"""
import sys
import turtle
sys.setExecutionLimit(35000)

def draw_spiral(t, angle):
    """Get turtle t to draw a spiral at an given angle"""

    for i in range(75):
        t.forward(i*2)
        t.left(angle)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("blue")
    tess.speed(20)
    
    tess.up()
    tess.goto(-100, 0)
    tess.down()
    draw_spiral(tess, 90)
    
    tess.up()
    tess.goto(100, 0)
    tess.down()
    draw_spiral(tess, 89)
    
    wn.exitonclick()
    
if __name__ == "__main__":
    main()

"""5. Write a non-fruitful function draw_equi_triangle(turtle, size) which calls draw_poly from the question above to have its turtle draw an equilateral triangle."""
import turtle

def draw_poly(t, sides, side_length):
    """Get turtle t to draw a polygon with sides sides that are side_length long"""

    for i in range(sides):
        t.forward(side_length)
        t.left(360/sides)

def draw_equi_triangle(turtle, size):
    """Get turtle t to draw a equilateral triangle with sides that are size long"""
    
    draw_poly(turtle, 3, size)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("hotpink")
    tess.pensize(3)
    
    draw_equi_triangle(tess, 50)
    
    wn.exitonclick()
    
if __name__ == "__main__":
    main()

"""6. Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and including n. So sum_to(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2."""
def sum_to(n):
    sum_n = (n * (n + 1)) / 2
    return int(sum_n)

def main():
    num = 10
    total = sum_to(num)
    print("The sum of the numbers from 1 to", num, "is:", total)
    
if __name__ == "__main__":
    main()

"""7. Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units."""
import turtle

def draw_star(t, length):
    #Draw star
    for i in range(5):
        t.forward(length)
        t.right(180 - (180 / 5))
    
def main():
    wn = turtle.Screen()

    #initialize Turtle
    star = turtle.Turtle()
    star.speed(3)
    
    draw_star(star, 100)

if __name__ == "__main__":
    main()

"""8. Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right by 144, put the pen down, and draw the next star. You’ll get something like this (note that you will need to move to the left before drawing your first star in order to fit everything in the window):"""
mport turtle

def draw_star(t, length):
    #Draw star
    for i in range(5):
        t.forward(length)
        t.right(180 - (180 / 5))
    
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    #initialize Turtle
    star = turtle.Turtle()
    star.color("hotpink")
    star.pensize(3)
    star.speed(3)
    
    distance = 100
    
    star.up()
    star.goto(-distance, -distance)
    star.down()
    draw_star(star, distance)
    
    star.up()
    star.goto(distance, -distance)
    star.down()
    draw_star(star, distance)
    
    star.up()
    star.goto(distance*1.5, 0)
    star.down()
    draw_star(star, distance)
    
    star.up()
    star.goto(0, distance)
    star.down()
    draw_star(star, distance)
    
    star.up()
    star.goto(-distance*1.5, 0)
    star.down()
    draw_star(star, distance)

if __name__ == "__main__":
    main()

#9. Extend the star function to draw an n pointed star. (Hint: n must be an odd number greater or equal to 3).
import turtle

def draw_nstar(t, length, points):
    #Draw star
    for i in range(points):
        t.forward(length)
        t.right(180 - (180 / points))
    
def main():
    
    n = int(input("how many points does the star have? (enter an odd integer > 3)"))
    wn = turtle.Screen()

    #initialize Turtle
    star = turtle.Turtle()
    star.speed(3)
    
    draw_nstar(star, 100, n)

if __name__ == "__main__":
    main()

"""10. Write a function called draw_sprite that will draw a sprite. The function will need parameters for the turtle, the number of legs, and the length of the legs. Invoke the function to create a sprite with 15 legs of length 120."""
import turtle

def draw_sprite(t, num_legs, length):
    #Draw sprite
    t.dot()
    for i in range(num_legs):
        t.forward(length)
        t.up()
        t.backward(length)
        t.down()
        t.right(360 / num_legs)
    
def main():
    wn = turtle.Screen()

    #initialize Turtle
    alex = turtle.Turtle()
    alex.speed(3)
    
    draw_sprite(alex, 15, 120)

if __name__ == "__main__":
    main()

#11. Rewrite the function sum_to(n) that returns the sum of all integer numbers up to and including n. This time use the accumulator pattern.
def sum_to(n):
    sum_n = 0
    
    for i in range(1, n+1):
        sum_n = sum_n + i
    return int(sum_n)

def main():
    num = 10
    total = sum_to(num)
    print("The sum of the numbers from 1 to", num, "is:", total)
    
if __name__ == "__main__":
    main()

#12. Write a function called fancy_square that will draw a square with fancy corners (sprites on the corners). You should implement and use the draw_sprite function from above.
import turtle

def draw_sprite(t, num_legs, length):
    #Draw sprite
    t.dot()
    for i in range(num_legs):
        t.forward(length)
        t.up()
        t.backward(length)
        t.down()
        t.right(360 / num_legs)
        
def fancy_square(f, length):
    for i in range(4):
        f.forward(length)
        draw_sprite(f, 15, (length/10))
        f.left(90)
        
def main():
    wn = turtle.Screen()

    #initialize Turtle
    alex = turtle.Turtle()
    alex.speed(3)
    
    fancy_square(alex, 100)

if __name__ == "__main__":
    main()


"""Weekly Graded Assignment

Write a function area_of_circle(r) which returns the area of a circle of radius r

As a refresher, the area of any circle is equal to the radius squared, multiplied by pi (where pi is 3.14159....).

Don’t forget to include the math module, where pi is defined.
"""
# TODO: use def to define a function called area_of_circle which takes an argument called r

    # TODO implement your function to return the area of a circle whose radius is r

import math
from test import testEqual

def area_of_circle(r):
    """Calculate the area of a circle, given the radius r"""
    
    area = math.pi * (r **2) # the area is pi * the radius squared
    return area
        
def main():
    
    val = area_of_circle(10)
    print("The area of the circle is:", val)

# Below are some tests which can give you an indication that your code seems to be correct.

# IMPORTANT: You should NOT include this part when you submit in Vocareum.
# When you submit, only include the function above.

t = area_of_circle(0)
testEqual(t, 0)
t = area_of_circle(1)
testEqual(t,math.pi)
t = area_of_circle(100)
testEqual(t, 31415.926535897932)
t = area_of_circle(-1)
testEqual(t, math.pi)
t = area_of_circle(-5)
testEqual(t, 25 * math.pi)
t = area_of_circle(2.3)
testEqual(t, 16.61902513749)

if __name__ == "__main__":
    main()