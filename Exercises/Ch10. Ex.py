#2. Create a list called my_list with the following six items: 76, 92.3, "hello", True, 4, 76. Do it with both append and with concatenation, one item at a time.
my_list = []

my_list.append(76)
my_list.append(92.3)
my_list.append("hello")
my_list.append(True)
my_list.append(4)
my_list.append(76)

print(my_list)

my_list2 = []

my_list2 += [76]
my_list2 += [92.3]
my_list2 += ["hello"]
my_list2 += [True]
my_list2 += [4]
my_list2 += [76]

print(my_list2)

"""3. Starting with the list in Exercise 2, write Python statements to do the following:

    Append “apple” and 76 to the list.
    Insert the value “cat” at position 3.
    Insert the value 99 at the start of the list.
    Find the index of “hello”.
    Count the number of 76s in the list.
    Remove the first occurrence of 76 from the list.
    Remove True from the list using pop and index.
"""
my_list = [76, 92.3, "hello", True, 4, 76]

my_list.append("apple")
my_list.append(76)
my_list.insert(3, "cat")
my_list.insert(0, 99)
print(my_list)
print(my_list.index("hello"))
print(my_list.count(76))
my_list.remove(76)
print(my_list)
my_list.pop(my_list.index(True))
print(my_list)

#Write a function to count how many odd numbers are in a list.
def count_odd(list):
    count = 0
    
    for item in list:
        item_type = str(type(item))
        if((item_type == "<class 'int'>") or (item_type == "<class 'float'>")):
            if item % 2 == 1:
                count += 1
                
    return count

print(count_odd([1, 1.0, 2, "Hi"]))

"""5. Write a Python function that will take a list of 100 random integers between 0 and 1000 (you can use iteration, append, and the random module to create a test list) and return the maximum value. (Note: there is a built-in function named max but do not use it for this exercise.)"""
import random

def max_num():
    nums = []
    
    for i in range(100):
        num = random.randrange(0 , 1000)
        nums.append(num)
    nums.sort()
    
    return nums[-1]

print(max_num())

"""6. Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:"""
def sum_of_squares(xs):
    square_sum = 0
    
    for num in xs:
        square_sum += (num ** 2)
    return square_sum
        
print(sum_of_squares([2, 3, 4]))

#7. Sum up all the negative numbers in a list.
def sum_neg(ns):
    sum_neg = 0
    
    for num in ns:
        if num < 0:
            sum_neg += num
            
    return sum_neg

print(sum_neg([-2, 3, -4, 6]))

#8. Count how many words in a list have length 5.
def len_of_words(lw):
    count = 0
    
    for word in lw:
        if len(word) == 5:
            count += 1
            
    return count

print(len_of_words(["dog", "happy", "five", "skate", "drive", "to"]))

"""9. Although Python provides us with many list methods, it is good practice and very instructive to think about how they are implemented. Implement your own Python functions that works like the following built-in ones:

    count
    in
    reverse
    index
    insert

Note that you cannot call your version of the in function “in”, since that is a reserved keyword. You could call it is_in instead."""
def count(ls, item):
    """Returns the number of occurrences of item"""
    count = 0
    
    for entry in ls:
        if entry == item:
            count += 1
    return count

def is_in(ls, item):
    """returns whether an item is in the list"""
    
    is_in = False
    for entry in ls:
        if entry == item:
            is_in = True
    return is_in
    
def reverse(ls):
    """Modifies a list to be in reverse order"""
    
    for i in range(len(ls)):
        temp = ls[i]
        ls[i] = ls[-(i + 1)]
        ls[-(i + 1)] = temp

def index(ls, item):
    """Returns the position of first occurrence of item"""
    index = 0
    
    for entry in ls:
        if entry == item:
            break
        else:
            index += 1
    return index

def insert(ls, position, item):
    """Inserts a new item at the position given"""
    new_item = item
    ls += [0]
    
    for i in range(position, len(ls)):
        temp = ls[i]
        ls[i] = new_item
        new_item = temp

mylist = [5, 27, 3, 12]
print(mylist)
insert(mylist, 1, 12)
print(mylist)
print(count(mylist, 12))

print(index(mylist, 3))
print(count(mylist, 5))
print(is_in(mylist, 27))

mylist.reverse()
print(mylist)

"""10. Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:

test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
test(replace(s, 'om', 'am'),
       'I love spam! Spam is my favorite food. Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!')

Hint: use the split and join methods."""
def replace(s, old, new):
    
    word_list = s.split(old)
    new_words = []
    for word in word_list:
        if word != (word_list[len(word_list)-1]):
            new_str = word + new
            new_words += new_str
        else:
            new_words += word
    return ("".join(new_words))
    
from test import testEqual

testEqual(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')
s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
testEqual(replace(s, 'om', 'am'), 'I love spam! Spam is my favorite food. Spam, spam, spam, yum!')
testEqual(replace(s, 'o', 'a'), 'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!')

#11. Write a function that will sum up all the elements in a list up to but not including the first even number.
def sum_of_initial_odds(nums):
    # your code here
    
    is_even = False
    index = 0
    sum_odd = 0
    
    while((is_even == False) and (index < len(nums))):
        if (nums[index] % 2) == 1:
            sum_odd += nums[index]
            index += 1
        else:
            is_even = True
    
    return sum_odd

from test import testEqual

testEqual(sum_of_initial_odds([1,3,1,4,3,8]), 5)
testEqual(sum_of_initial_odds([6,1,3,5,7]), 0)
testEqual(sum_of_initial_odds([1, -7, 10, 23]), -6)
testEqual(sum_of_initial_odds(range(1,555,2)), 76729)


"""Weekly Graded Assignment

Write a function that will return a string of country codes from an argument that is a string of prices (containing dollar amounts following the country codes). Your function will take as an argument a string of prices like the following: "US$40, AU$89, JP$200". In this example, the function would return the string "US, AU, JP".

Hint: You may want to break the original string into a list, manipulate the individual elements, then make it into a string again.
"""

def sum_of_initial_odds(nums):
    # your code here
    
    is_even = False
    index = 0
    sum_odd = 0
    
    while((is_even == False) and (index < len(nums))):
        if (nums[index] % 2) == 1:
            sum_odd += nums[index]
            index += 1
        else:
            is_even = True
    
    return sum_odd

from test import testEqual

testEqual(sum_of_initial_odds([1,3,1,4,3,8]), 5)
testEqual(sum_of_initial_odds([6,1,3,5,7]), 0)
testEqual(sum_of_initial_odds([1, -7, 10, 23]), -6)
testEqual(sum_of_initial_odds(range(1,555,2)), 76729)
