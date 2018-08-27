""" 1. Below is a short program that prompts the user to input the number of miles they are to drive on a given trip and converts their answer to kilometers, printing the result. However, it doesn’t work properly. Find and fix the error in the program.
miles = input("How many miles do you have to drive? ")

kilometers = miles * 1.60934

print("That distance is equal to", kilometers, "kilometers")
"""
miles = input("How many miles do you have to drive? ")
miles = float(miles)

kilometers = miles * 1.60934

print("That distance is equal to", kilometers, "kilometers")

""" 2. Picture a compass where 0 degrees represents North, 90 degrees represents East, and so on, all the way around to 360 degrees, which is again the same as 0 degrees: true north.

The program below envisions the scenario in which a person is facing North (aka 0 degrees) and spins some number of rotations, either clockwise or counter-clockwise (-1 represents a full counter-clockwise spin and 1 represents a full clockwise spin). It calculates the direction they end up facing in degrees. However, it doesn’t work properly. Find and fix the error in the program.

spins = input("How many times did you spin? (Enter a negative number for counter-clockwise spins) ")

degrees = float(spins) * 360

print("You are facing", degrees, "degrees relative to north")
"""
spins = input("How many times did you spin? (Enter a negative number for counter-clockwise spins) ")

degrees = float(spins) * 360
if degrees < 0:
    degrees = 360 + degrees
    
quad = degrees // 90

if quad == 0:
    direction = "North"
if quad == 1.0:
    direction = "East"    
if quad == 2.0:
    direction = "South"
if quad == 3.0:
    direction = "West"

if quad == 4.0:
    print("You are facing 0 degrees relative to north")
else:
    print("You are facing", (degrees % 90), "degrees relative to", direction)

""" 3. ou’ve written a program to convert degrees Celsius to degrees Fahrenheit. The program below makes the conversion in the opposite direction, from Fahrenheit to Celsius. However, it doesn’t work properly. Find and fix the error in the program.

current_temp_string = input("Enter a temperature in degrees Fahrenheit: ")
current_temp = int(current_temp_string)

current_temp_celsius = (current_tmp - 32) * (5/9)
print("The temperature in Celsius is:", current_temp_celsius)
"""
current_temp_string = input("Enter a temperature in degrees Fahrenheit: ")
current_temp = int(current_temp_string)

current_temp_celsius = (current_temp - 32) * (5/9)
print("The temperature in Celsius is:", current_temp_celsius)

""" 4. Football Scores Suppose you’ve written the program below. The given program asks the user to input the number of touchdowns and field goals scored by an American football team, and prints out the team’s score. (We generously assume that for each touchdown, the team always makes the extra point.)

The European Union has decided that they want to start an American football league, and they want to use your killer program to calculate scores, but they like things that are multiples of 10 (e.g. the Metric System), and have decided that touchdowns will be worth 10 points (including the extra point they might score) and field goals are worth 5 points. Modify the program below to work on both continents, and beyond. It should ask the user how many points a touchdown is worth and how many points a field goal is worth. Then it should ask in turn for both the number of touchdowns and the number of field goals scored, and then print the team’s total score.

num_touchdowns = input("How many touchdowns were scored? ")
num_field_goals = input("How many field goals were scored? ")

total_score = 7 * int(num_touchdowns) + 3 * int(num_field_goals)

print("The team has", total_score, "points")
"""
num_touchdowns = input("How many touchdowns were scored? ")
num_field_goals = input("How many field goals were scored? ")
continent = input('''Is this game for the European Union? (If so, enter "Y")''')

if continent == "Y":
    total_score = 10 * int(num_touchdowns) + 5 * int(num_field_goals)
else:
    total_score = 7 * int(num_touchdowns) + 3 * int(num_field_goals)

print("The team has", total_score, "points")

"""Weekly Graded Assignment

This is a tricky one!

You have a thermostat that allows you to set the room to any temperature between 40 and 89 degrees.

The thermostat can be adjusted by turning a circular dial. For instance, if the temperature is set to 50 degrees and you turn the dial 10 clicks toward the left, you will set the temperature to 40 degrees. But if you keep turning 1 click to the left (represented as -1) it will circle back around to 89 degrees. If you are at 40 degrees and turn to the right by one click, you will get 41 degrees. As you continue to turn to the right, the temperature goes up, and the temperature gets closer and closer to 89 degrees. But as soon as you complete one full rotation (50 clicks), the temperature cycles back around to 40 degrees.

Write a program that calculates the temperature based on how much the dial has been turned. The number of clicks (from the starting point of 40 degrees) is contained in a variable. You should print the current temperature for each given click variable so that your output is as follows:

The temperature is 40
The temperature is 89
The temperature is 64
The temperature is 41
The temperature is 89
The temperature is 40
"""

#For each click variable, calculate the temperature and print it as shown in the instructions
temp = 40
reset = False

click_1 = 0
# TODO calculate the temperature, and report it back to the user
if click_1 == -1:
    temp = 89
    reset = True
if click_1 // 50 > 0:
    temp = 40
    click_1 = click_1 % 50


new_temp = temp + click_1
if reset == False:
    if new_temp > 89:
        temp = 40 + (new_temp - 89)
    else:
        if new_temp < 40:
            temp = 89 - (40 - new_temp)
        else:
            temp = new_temp
print("The temperature is", temp)
reset = False

click_2 = 49
# TODO calculate the temperature, and report it back to the user
if click_2 == -1:
    temp = 89
    reset = True
if click_1 // 50 > 0:
    temp = 40
    click_2 = click_2 % 50


new_temp = temp + click_2
if reset == False:
    if new_temp > 89:
        temp = 40 + (new_temp - 89)
    else:
        if new_temp < 40:
            temp = 89 - (40 - new_temp)
        else:
            temp = new_temp
print("The temperature is", temp)
reset = False

click_3 = 74
# TODO calculate the temperature, and report it back to the user
if click_3 == -1:
    temp = 89
    reset = True
if click_3 // 50 > 0:
    temp = 40
    click_3 = click_3 % 50


new_temp = temp + click_3
if reset == False:
    if new_temp > 89:
        temp = 40 + (new_temp - 89)
    else:
        if new_temp < 40:
            temp = 89 - (40 - new_temp)
        else:
            temp = new_temp
print("The temperature is", temp)
reset = False

click_4 = 51
# TODO calculate the temperature, and report it back to the user
if click_4 == -1:
    temp = 89
    reset = True
if click_4 // 50 > 0:
    temp = 40
    click_4 = click_4 % 50


new_temp = temp + click_4
if reset == False:
    if new_temp > 89:
        temp = 40 + (new_temp - 89)
    else:
        if new_temp < 40:
            temp = 89 - (40 - new_temp)
        else:
            temp = new_temp
print("The temperature is", temp)
reset = False

click_5 = -1
# TODO calculate the temperature, and report it back to the user
if click_5 == -1:
    temp = 89
    reset = True
if click_5 // 50 > 0:
    temp = 40
    click_5 = click_5 % 50


new_temp = temp + click_5
if reset == False:
    if new_temp > 89:
        temp = 40 + (new_temp - 89)
    else:
        if new_temp < 40:
            temp = 89 - (40 - new_temp)
        else:
            temp = new_temp
print("The temperature is", temp)
reset = False

click_6 = 200
# TODO calculate the temperature, and report it back to the user
if click_6 == -1:
    temp = 89
    reset = True
if click_6 // 50 > 0:
    temp = 40
    click_6 = click_6 % 50


new_temp = temp + click_6
if reset == False:
    if new_temp > 89:
        temp = 40 + (new_temp - 89)
    else:
        if new_temp < 40:
            temp = 89 - (40 - new_temp)
        else:
            temp = new_temp
print("The temperature is", temp)
