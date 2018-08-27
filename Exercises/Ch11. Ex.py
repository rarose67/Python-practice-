"""1. Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample run of the program might look like this:

Please enter a sentence: ThiS is a String with Upper and lower case Letters.
a  3
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2
$
"""
def create_dict(str):
    
    my_dict = {}
    
    for letter in str:
        if letter.isalpha():
            letter = letter.lower()
            if letter not in my_dict:
                my_dict[letter] = 1
            else:
                my_dict[letter] += 1
                
    return my_dict
                
def print_dict(my_dict):
    keys = list(my_dict.keys())
    keys.sort()
    for key in keys:
        print(key, " ", my_dict[key])

def main():
    text = input("Please enter a sentence: ")
    chars = create_dict(text)
    print_dict(chars)
    
if __name__ == "__main__":
    main()

"""2. Write a program that will function as a grade book, allowing a user (a professor or teacher) to enter the class roster for a course, along with each student’s cumulative grade. It then prints the class roster along with the average cumulative grade. Grades are on a 0-100 percentage scale. Use 2 lists (grades and students) and the enumerate function in your solution.

A test run of this program would yield the following:

# this is the first batch of input the user would enter
Chris
Jesse
Sally

# this is the second batch of input the user would enter
Grade for Chris: 90
Grade for Jesse: 80
Grade for Sally: 70

# below is what your program should output
Class roster:
Chris (90.0)
Jesse (80.0)
Sally (70.0)

Average grade: 80.0
"""
import sys
sys.setExecutionLimit(70000)

students = []
grades = []
total_score = 0.0

name = input("Enter the name of a student.  (When finished, enter nothing)")
while (name != ""):
    students += [name]
    name = input("Enter the name of a student.  (When finished, enter nothing)")

for i in range(len(students)):
    score = float(input("Grade for {0}:".format(students[i])))
    grades += [score]
    
print("Class roster:")
for index, student in enumerate(students):
    total_score += grades[index]
    print("{0} ({1:.1})".format(student, grades[index]))
    
print("\nAverage grade:", (total_score / len(students)))

#3. Implement the functionality of the above program using a dictionary instead of a list.
import sys
sys.setExecutionLimit(70000)

students = {}
total_score = 0.0

name = input("Enter the name of a student.  (When finished, enter nothing)")
while (name != ""):
    students[name] = 0.0
    name = input("Enter the name of a student.  (When finished, enter nothing)")

print("Class roster:")
for student in students.keys():
    score = float(input("Grade for {0}:".format(student)))
    students[student] = score
    total_score += students[student]
    print("{0} ({1:.1})".format(student, students[student]))
    
print("\nAverage grade:", (total_score / len(students)))

"""4. Make a dictionary where the key is a worker’s name, and the value is a list where the first element is the clock in time, second element is the clock out time, and the third element is the total hours worked that day. Each worker’s list starts at [0, 0, 0]. Create functions for clock_in and clock_out.

    clock_in takes the dictionary of workers, the name of the worker, and the clock in time as parameters. When the worker clocks in, enter and save their clock in time as the first element in the associated list value.
    clock_out takes the same parameters, but with a clock out time instead of clock in time. When the worker clocks out, enter and save their clock out time and calculate the hours worked for that day and store it as the third element in the list.

To make this program a little easier, we’re entering the clock in and clock out times as integers. As a bonus mission, try adding the times as strings representing the 24 hour clock (e.g., "08:00"), and then figure out how to calculate the time worked. And you can do this exercise either by aliasing or copying the dictionary."""
def clock_in(worker_dict, name, clock_in_time):
    
    worker_dict[name][0] = clock_in_time
    
def clock_out(worker_dict, name, clock_out_time):
    
    worker_dict[name][1] = clock_out_time
    worker_dict[name][2] = clock_out_time - worker_dict[name][0]
    
def main():
    workers = {"George Spelvin": [0,0,0], "Jane Doe": [0,0,0], "John Smith": [0,0,0]}
    print(workers.get("George Spelvin"))   # should print [0,0,0]
    clock_in(workers, "George Spelvin", 8)
    clock_out(workers, "George Spelvin", 17)
    print(workers.get("George Spelvin"))   # should print [8, 17, 9]

if __name__ == "__main__":
    main()

"""5. Here’s a table of English to Pirate translations:
English 	Pirate
sir 	matey
hotel 	fleabag inn
student 	swabbie
boy 	matey
madam 	proud beauty
professor 	foul blaggart
restaurant 	galley
your 	yer
excuse 	arr
students 	swabbies
are 	be
lawyer 	foul blaggart
restroom 	th’ head
my 	me
hello 	avast
is 	be
man 	matey

Write a program that asks the user for a sentence in English and then translates that sentence to Pirate."""
from test import testEqual

def translate(text):
    # your code here!
    pirate_text = ""
    
    my_dict = {"sir" : "matey", "hotel" : "fleabag inn", "student" : "swabbie", "boy" : "matey", 
               "madam" : "proud beauty", "professor" : "foul blaggart", "restaurant" : "galley",
               "your" : "yer", "excuse" : "arr", "students" : "swabbies", "are" : "be", 
               "lawyer" : "foul blaggart", "restroom" : "head", "my" : "me", "the" : "th'",
               "hello" : "avast", "is" : "be", "man" : "matey"}
    
    word_list = text.split()
    index = 0
    pirate_words = []
    for word in word_list:
        char = ""
        pirate_word = ""
        if (word.isalpha() == False):
            char = word[len(word)-1]
            new_word = word[:len(word)-1]
        else:
            new_word = word
        #print("!"+new_word+"!")
        if new_word in my_dict:
            pirate_word = my_dict[new_word] 
        else:
            pirate_word = new_word
        
        pirate_word += char
        index += 1
        pirate_words += [pirate_word]
        
    pirate_text = " ".join(pirate_words)
    #print(my_dict, "\n\n")
    print(pirate_text)
    return pirate_text
           
text = "hello my man, please excuse your professor to the restroom!"
testEqual(translate(text), "avast me matey, please arr yer foul blaggart to th' head!")

"""6. Give the Python interpreter’s response to each of the following from a continuous interpreter session:

    >>> d = {'apples': 15, 'bananas': 35, 'grapes': 12}
    >>> d['bananas']

    >>> d['oranges'] = 20
    >>> len(d)

    >>> 'grapes' in d

    >>> d['pears']

    >>> d.get('pears', 0)

    >>> fruits = d.keys()
    >>> sorted(fruits)
    >>> print(fruits)

    >>> del d['apples']
    >>> 'apples' in d

Be sure you understand why you get each result. """
from test import testEqual

# Note: The pass is a placeholder to allow
# the code to compile. Remove it when you
# begin coding.
def set_inventory(inventory, fruit, quantity=0):
    inventory[fruit] = quantity

# make these tests work...
new_inventory = {}
set_inventory(new_inventory, 'strawberries', 10)
testEqual('strawberries' in new_inventory, True)
testEqual(new_inventory['strawberries'], 10)
set_inventory(new_inventory, 'strawberries', 25)
testEqual(new_inventory['strawberries'] , 25)


"""Weekly Graded Assignment

Write a sort_contacts function that takes a dictionary of contacts as a parameter and returns a sorted list of those contacts, where each contact is a tuple.

The contacts dictionary that will be passed into the function has the contact name as its key, and the value is a tuple containing the phone number and email for the contact.

contacts = {name: (phone, email), name: (phone, email), etc.}

The sort_contacts function should then create a new, sorted (by last name) list of tuples representing all of the contact info (one tuple for each contact) that was in the dictionary. It should then return this list to the calling function.

For example, given a dictionary argument of:

{"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
"Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
"Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}

sort_contacts should return this:

[('Freud, Anna', '1-541-754-3010', 'anna@psychoanalysis.com'), ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'), ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')]
"""

# Create sort_contacts function
def sort_contacts(contacts):
    """Sorts a dictionary of contacts"""
    
    key_list = list(contacts.keys())  #get keys
    key_list.sort()  #sort key_list
    sorted_list = []  #initialize sorted list
    for key in key_list:
        contact = (key, contacts[key][0], contacts[key][1])  #create tuple
        sorted_list += [contact] #add tuple to list
    
    return(sorted_list)

# The code below is just for your testing purposes. Make sure you pass all the tests.
# In Vocareum, only put code for the sort_contacts function above
from test import testEqual

testEqual(sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}), [('Freud, Anna', '1-541-754-3010',
        'anna@psychoanalysis.com'), ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
        ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')])
testEqual(sort_contacts({"Summitt, Pat": ("1-865-355-4320", "pat@greatcoaches.com"),
    "Rudolph, Wilma": ("1-410-5313-584", "wilma@olympians.com")}),
    [('Rudolph, Wilma', '1-410-5313-584', 'wilma@olympians.com'),
    ('Summitt, Pat', '1-865-355-4320', 'pat@greatcoaches.com')])
testEqual(sort_contacts({"Dinesen, Isak": ("1-718-939-2548", "isak@storytellers.com")}),
    [('Dinesen, Isak', '1-718-939-2548', 'isak@storytellers.com')])
testEqual(sort_contacts({"Rimbaud, Arthur": ("1-636-555-5555", "arthur@notlive.com"),
    "Swinton, Tilda": ("1-917-222-2222", "tilda@greatActors.com"),
    "Almodovar, Pedro": ("1-990-622-3892", "pedro@filmbuffs.com"), "Kandinsky, Wassily":
    ("1-333-555-9999", "kandinsky@painters.com")}), [('Almodovar, Pedro', '1-990-622-3892',
    'pedro@filmbuffs.com'), ('Kandinsky, Wassily', '1-333-555-9999', 'kandinsky@painters.com'),
    ('Rimbaud, Arthur', '1-636-555-5555', 'arthur@notlive.com'), ('Swinton, Tilda',
    '1-917-222-2222', 'tilda@greatActors.com')])
