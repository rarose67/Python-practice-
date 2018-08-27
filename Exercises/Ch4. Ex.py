"""1. Write a program that prints We like Python's turtles! 1000 times.

Now, update that program to prompt the user for an integer and then print the same message the given number of times."""
num = int(input("How many times should the message be printed?"))

for i in range(num):
    print("We like Python's turtles!")

""" 2. Write a program that prints out the lyrics to the song “99 Bottles of Beer on the Wall”"""
for i in range(99, 0, -1):
    print(i, "bottles of beer on the wall!")
    print(i, "bottles of beer!")
    print("Take one down, pass it around")
    print(i - 1, "bottles of beer on the wall!\n")

#3. Write a program that prints even integers from 0 to 50.
for i in range(0, 51, 2):
    print(i)

"""4. 
Write a program that uses a for loop to print
    One of the months of the year is January
    One of the months of the year is February
    One of the months of the year is March
    etc ...
"""
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]

for month in months:
    print("One of the months of the year is", month)

"""5. Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

    An equilateral triangle
    A square
    A hexagon (six sides)
    An octagon (eight sides)
"""
import turtle
wn = turtle.Screen()

lenth = 50

#initialize Turtles
zelda = turtle.Turtle()
square = turtle.Turtle()
hexagon = turtle.Turtle()
octagon = turtle.Turtle()

#Draw Triangle
for i in range(3):
    zelda.forward(lenth)
    zelda.right(360/3)
zelda.clear()

#Draw Square
for i in range(4):
    square.forward(lenth)
    square.right(360/4)
square.clear()

#Draw Hexagon
for i in range(6):
    hexagon.forward(lenth)
    hexagon.right(360/6)
hexagon.clear()

#Draw Octagon
for i in range(8):
    octagon.forward(lenth)
    octagon.right(360/8)

""" 6. Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of a regular polygon."""
import turtle
wn = turtle.Screen()

sides = int(input("How many sides does your polygon have?"))
lenth = float(input("How long is each side?"))
border_color = input("What color is each side?")
fill_color = input("What color is the inside of the polygon?")

#initialize Turtle
polygon = turtle.Turtle()
polygon.pencolor(border_color)
polygon.fillcolor(fill_color)
polygon.speed(1)

#Draw polygon
polygon.begin_fill()
for i in range(sides):
    polygon.forward(lenth)
    polygon.right(360/sides)
polygon.end_fill()

wn.exitonclick()

"""7. A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend."""
#import modules
import turtle

# initialize screen & turtle
wn = turtle.Screen()
pirate = turtle.Turtle()

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

# draw route
pirate.forward(100)
for turn in turns:
    pirate.left(turn)
    pirate.forward(100)

#9.
import turtle
wn = turtle.Screen()

#initialize Turtle
polygon = turtle.Turtle()
polygon.speed(3)

points = 5

#Draw polygon
for i in range(points):
    polygon.forward(100)
    polygon.right(180 - (180 / points))

#10. Write a program to draw a face of a clock
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.penup()

for i in range(10):
    tess.forward(80)
    tess.pendown()
    tess.forward(10)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.backward(110)
    tess.right(36)
                 
#12. Create a turtle and assign it to a variable. When you print its type, what do you get?
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
t = type(tess)
print(t)

"""13. A sprite is a simple spider shaped thing with n legs coming out from a center point. The angle between each leg is 360 / n degrees.

Write a program to draw a sprite where the number of legs is provided by the user."""
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.dot()

legs = int(input("How many legs?"))

for leg in range(legs):
    tess.right(360/legs)
    tess.forward(50)
    tess.penup()
    tess.goto(0, 0)
    tess.pendown()

#14. Use a for statement to print 10 random numbers.
import random

for i in range(10):
    num = random.random()
    print(num)

#15. Repeat the above exercise but this time print 10 random numbers between 25 and 35.
import random

for i in range(10):
    num = random.randrange(25, 36)
    print(num)

"""16. The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle is related to the lengths of the other two sides. Look through the math module and see if you can find a function that will compute this relationship for you. Once you find it, write a short program to try it out."""
import math

side = math.hypot(2, 3) 
print(side)

"""17. Search on the internet for a way to calculate an approximation for pi. There are many that use simple arithmetic. Write a program to compute the approximation and then print that value as well as the value of math.pi from the math module."""
import math
import random

rand = random.random()
sign = random.randrange(-1, 1)
x = rand * sign

pi_aprox = 2 *(math.asin(math.sqrt(1-x ** 2)) + fabs(math.asin(x)))

print("Pi approx. is", pi_aprox)
print("\nmath.pi is", math.pi)
print("\n The dif is", pi_aprox - math.pi) 


"""Weekly Graded Assignment

Assume you have a list of numbers nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

    Write a loop that prints each of the numbers on a new line, like this:

    12
    10
    ...etc

    Write a second loop that prints each number and its square on a new line, precisely like this:

    The square of 12 is 144
    The square of 10 is 100
    ...etc
"""

nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for num in nums:
    print(num)

print("\n")

for num in nums:
    print("The square of", num, "is", num ** 2)