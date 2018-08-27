""" 1. Evaluate the following numerical expressions in your head, then use the active code window to check your results:

    5 ** 2
    9 * 5
    15 / 12
    12 / 15
    15 // 12
    12 // 15
    5 % 2
    9 % 5
    15 % 12
    12 % 15
    6 % 6
    0 % 7
"""

print("1.  ", 5 ** 2)
print("2.  ", 9 * 5)
print("3.  ", 15 / 12)
print("4.  ", 12 / 15)
print("5.  ", 15 // 12)
print("6.  ", 12 // 15)
print("7.  ", 5 % 2)
print("8.  ", 9 % 5)
print("9.  ", 15 % 12)
print("10.  ", 12 % 15)
print("11.  ", 6 % 6)
print("12.  ", 0 % 7)

""" 2. What is the order of the arithmetic operations in the following expression? Evaluate the expression by hand and then check your work.

2 + (3 - 1) * 10 / 5 * (2 + 3)
"""

num = 2 + (3 - 1) * 10 / 5 * (2 + 3)
print(num) 

""" 3. Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).

If it is currently 13 and you set your alarm to go off in 50 hours, the hour will be 15 (3pm). Write a program to solve the general version of the above problem. Ask the user for the current time (in hours), and then ask for the number of hours to wait for the alarm.

Your program should output what the hour will be on the clock when the alarm goes off.
"""

cur_hour = int(input("What time is it (in hours)?"))
hrs_wait = int(input("In how many hours should the alarm sound?"))
new_hour = (cur_hour + hrs_wait) % 24
print("The alarm will sound at hour", new_hour)

""" 4. Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print."""

first_word = "All"
second_word = "work"
third_word = "and"
fourth_word = "no"
fith_word = "play"
sixth_word = "makes"
seventh_word = "Jack"
eigth_word = "a"
ninth_word = "dull"
last_word = "boy"
print(first_word, second_word, third_word, fourth_word, fith_word, sixth_word, seventh_word, eigth_word,
      ninth_word, last_word + ".")

""" 5. Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6."""

print(6 * (1 - 2))

""" 6. The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
formula for compound interest

Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.
"""

P = 10000
n = 12
r = 0.08
t = int(input("How many years will the money compound for?"))
final_amount = P * ((1 + (r / n)) ** (n * t))
print("After", t, "years, you'll have $", final_amount) 

""" 7. Write a program that will compute the area of a circle. Prompt the user to enter the radius, and then print the answer, like this:

What is the radius of your circle?
>>> 7.8
191.0376
"""

radius = float(input("What is the radius of your circle?"))
pi =3.14159
area = pi * radius ** 2
print(area)

""" 8. Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. Print a nice message with the answer."""

width = float(input("Enter the width of the rectangke."))
height = float(input("Enter the height of the rectangke."))
area = height * width
print("The aera of the rectangle is", area)

""" 9. Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer, like this:

How many miles have you driven?
>>> 150
How many gallons have you used?
>>> 5
Your car gets 30 miles per gallon.
"""

miles_driven = int(input("How many miles have you driven?"))
gallons = int(input("How many gallons have you used?"))
miles_per_gallon = miles_driven // gallons
print("Your car gets", miles_per_gallon, "miles per gallon.")

""" 10. Write a program that will convert degrees Celsius to degrees Fahrenheit."""

deg_c = float(input("What is the temperature in Celsius?"))
deg_f = deg_c * (9 / 5) + 32
print(deg_c, "degrees Celsius is", deg_f, "degress Fahrenheit.")

""" 11. Write a program that will convert degrees Fahrenheit to degrees Celsius, like this:

What is the temperature in Fahrenheit?
>>> 32
32.0 degrees Fahrenheit is 0.0 degrees Celsius.
"""
deg_f = float(input("What is the temperature in Fahrenheit?"))
deg_c = (deg_f - 32) * (5 / 9)
print(deg_f, "degrees Fahrenheit is", deg_c, "degress Celsius.")
