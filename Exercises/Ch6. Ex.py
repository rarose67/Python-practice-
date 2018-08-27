#1. What do these expressions evaluate to?
print("3 == 3 is:", 3 == 3)
print("3 != 3 is:", 3 != 3)
print("3 >= 4 is:", 3 >= 4)
print("not(3 < 4) is:", not(3 < 4))

"""2. Write a function which is given an exam score, and it returns the corresponding letter grade as a string according to this scheme:
score 	Grade
>= 90 	A
[80-90) 	B
[70-80) 	C
[60-70) 	D
< 60 	F

The square and round brackets denote closed and open intervals, respectively. A closed interval includes the number, an open interval excludes it. So 79.99999 gets grade C , but 80 gets grade B.

Test your function by printing the score and the grade for a number of different scores."""
def grade(score):
    if score < 60.0:
        grade = "F"
    elif score < 70.0:
        grade = "D"
    elif score < 80.0:
        grade = "C"
    elif score < 90.0:
        grade = "B"
    else:
        grade = "A"
        
    return grade

def main():

    scores = [100, 80, 75, 60, 59.9]

    for i in scores:
        score = float(i)
        letter_grade = grade(score)
        print("The grade for a score of", score, "is:", letter_grade)
    
if __name__ == "__main__":
    main()

"""3. Modify the turtle bar chart program from the previous chapter so that the bar for any value of 200 or more is filled with red, values between [100 and 200) are filled yellow, and bars representing values less than 100 are filled green."""
import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        t.fillcolor("red")
    elif height >= 100:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def main():
    data = [48, 117, 200, 240, 160, 260, 220]
    max_height = max(data)
    num_bars = len(data)
    border = 10

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0-border, 0-border, 40 * num_bars + border, max_height + border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.pensize(3)

    for x in data:
        draw_bar(tess, x)

    wn.exitonclick()

if __name__ == "__main__":
    main()

"""4. In the Turtle bar chart program, what do you expect to happen if one or more of the data values in the list is negative? Go back and try it out. Then change the program so that when it prints the text value for the negative bars, it puts the text above the base of the bar (on the 0 axis)."""
import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    if (height < 0):
        t.write(str(height))
    t.left(90)
    t.forward(height)
    if (height >= 0):
        t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def main():
    data = [48, -117, 200, 240, 160, 260, 220]
    max_height = max(data)
    num_bars = len(data)
    border = 10

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0-border, 0-border, 40 * num_bars + border, max_height + border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)

    for x in data:
        draw_bar(tess, x)

    wn.exitonclick()

if __name__ == "__main__":
    main()

"""5. Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd. Note that instead of printing out the results we are using test statements. The goal is to pass all the tests that are listed underneath the function you will write. You do not need to add a main function to this code to run it."""
from test import testEqual

def is_even(n):
    # your code here
    if (n % 2) == 0:
        return True
    else:
        return False

testEqual(is_even(10), True)
testEqual(is_even(5), False)
testEqual(is_even(1), False)
testEqual(is_even(0), True)

#6. Now write the function is_odd(n) that returns True when n is odd and False otherwise.
from test import testEqual

def is_odd(n):
    # Your code here
     # your code here
    if (n % 2) != 0:
        return True
    else:
        return False

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)

#7. Modify is_odd so that it uses a call to is_even to determine if its argument is an odd integer.
from test import testEqual

def is_even(n):
    # your code here
    if (n % 2) == 0:
        return True
    else:
        return False
    
def is_odd(n):
    # your code here
   
    if not(is_even(n)):
        return True
    else:
        return False

testEqual(is_odd(10), False)
testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(0), False)

"""8. Write a fruitful function called pick_activity to help you pick an activity to engage in based on the current weather. It has two parameters, one for how hot it is and one for how wet it is. If it is hot and wet, it should tell you to watch Netflix. If it hot and dry, it should tell you to go swimming. If it is cold and wet, it should tell you to paint. If it is cold and dry, it should tell you to go to a cafe and read. Use the elif construct."""
def pick_activity(temp, humidity):
    """pick an activity based on temp & humidity."""
    if temp > 50:
        hot = True
        cold = False
    else:
        hot = False
        cold = True
        
    if(humidity >= 50):
        wet = True
        dry = False
    else:
        wet = False
        dry = True
        
    if(hot and wet):
        activity = "Watch Netflix."
    elif(hot and dry):
        activity = "Go swimming."
    elif(cold and wet):
        activity = "paint the house."
    elif(cold and dry):
        activity = "go to a cafe and read."
        
    return activity

to_do = pick_activity(51, 50)
print(to_do)
to_do = pick_activity(0, 50)
print(to_do)
to_do = pick_activity(75, 35)
print(to_do)
to_do = pick_activity(32, 5)
print(to_do)
    
"""9. Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up using the abs() function like so:

if  abs(x - y) < 0.001:      # if x is approximately equal to y
    ...
"""
import math
from test import testEqual

def is_rightangled(a, b, c):
    # your code here
    
    hyp = math.hypot(a, b)
    print("dif is:", abs(c - hyp)) 
    
    if  abs(c - hyp) < 0.0001:      # if x is approximately equal to y
        return True
    else:
        return False
    
testEqual(is_rightangled(1.5, 2.0, 2.5), True)
print("\n")
testEqual(is_rightangled(4.0, 8.0, 16.0), False)
print("\n")
testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
print("\n")
testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
print("\n")
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
print("\n")
testEqual(is_rightangled(0.5, 0.4, 0.64031), True)

#10. Extend the above program so that the sides can be given to the function in any order.
import math
from test import testEqual

def is_rightangled(a, b, c):
    # your code here
    
    long_side = max([a, b, c])
    
    if  abs(a - long_side) < 0.0001:      # if a is the longest side
        hyp = math.hypot(b, c)
    elif  abs(b - long_side) < 0.0001:    # if b is the longest side
        hyp = math.hypot(a, c)
    else:                                 # if c is the longest side
        hyp = math.hypot(a, b)
        
    print("dif is:", abs(long_side - hyp))
    
    if  abs(long_side - hyp) < 0.0001:      # if x is approximately equal to y
        return True
    else:
        return False

testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(16.0, 4.0, 8.0), False)
testEqual(is_rightangled(4.1, 9.1678787077, 8.2), True)
testEqual(is_rightangled(9.16787, 4.1, 8.2), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.64031, 0.4), True)

"""11. Implement the calculator for the date of Easter.

The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.

Ask the user to enter a year. Compute the following:

    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    date = 22 + d + e

Special note: The algorithm can give a date greater than 31 (the number of days in March). When this happens, it signifies a date in April. Thus, 32 is April 1, 35 is April 4, and so on. Also, if the year is one of four special years (1954, 1981, 2049, or 2076) then subtract 7 from the date.

Your program should print an error message if the user provides a date that is out of range."""
def date_of_easter(year):
    # Your code here
    a = year % 19
    b = year % 4
    c = year % 7
    
    
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    date = 22 + d + e
    
    if ((year == 1954) or (year == 1981) or (year == 2049) or (year == 2076)):
        date -= 7
        
    if (date % 31) > 0:
        print("Easter in the year", year, "is on April", (date % 31))
    else:
        print("Easter in the year", year, "is on March", date)
    
    
    
    

def main():
    # Your code here
    year = input("Please enter a year between 1900 to 2099.")
    year = int(year)
    
    if((year >= 1900) and (year <= 2099)):  
        date_of_easter(year)
    else:
        print("You enter an invalid year.  This program only calculate the date of Easter",
              "for a year between 1900 to 2099")
              
        
    

if __name__ == "__main__":
    main()


"""Weekly Graded Assignment

A year is a leap year if it is divisible by 4, unless it is a century that is not divisible by 400.

For example:

    1956 is a leap year because 1956 is divisible by 4.
    1957 is not a leap year, because it is not divisible by 4.
    1900 is not a leap year, despite the fact that it is divisible by 4, because 1900 is a century and 1900 is not divisible by 400.
    1600 is a leap year, because 1600 is divisible by 4 and 1600 is divisible by 400

Write a function is_leap that takes a year as a parameter and returns True if the year is a leap year, False otherwise.
"""

def is_leap(year):
    """ Determine if a year is a leap year"""
    
    four_century  = ((year % 400) == 0)  #Is the year divisible by 400
    century  = ((year % 100) == 0)       #Is the year the start of a century
     
    if (year % 4) == 0:
        if(century and not(four_century)):
            return False                 # A century year that isn't divisible by 400, isn't a leap year.
        else:
            return True
    else:
        return False
    
# Below is a set of tests so you can check if your code is correct.
# Do not copy this part into Vocareum.
from test import testEqual

testEqual(is_leap(1944), True)
testEqual(is_leap(2011), False)
testEqual(is_leap(1986), False)
testEqual(is_leap(1956), True)
testEqual(is_leap(1957), False)
testEqual(is_leap(1800), False)
testEqual(is_leap(1900), False)
testEqual(is_leap(1600), True)
testEqual(is_leap(2056), True)
