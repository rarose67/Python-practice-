"""
It is possible to name the days 0 through 6, where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day 3 (a Wednesday) and you return home after 10 nights, you arrive home on day 6 (a Saturday).

Write a general version of the program which asks for the day number that your vacation starts on and the length of your holiday, and then tells you the number of the day of the week you will return on.
"""

#difine a list of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#ask user for start day 
start_day = int(input("What day of the week does your vacation start?" +
                "(use 0 for Sunday, 6 for Saturday, etc.)"))  
#ask user for the lenth of the vacation
vac_length = int(input("How long is your vacation?"))
#determine what day you'll return
last_day = (start_day + vac_length) % 7
#output your return day
print("You'll return on", days[last_day])