"""
Since a string is just a sequence of characters, they can be sorted from least to greatest. Sorting can be hard so we’re just going to check if a string is sorted. Write a function which returns a boolean indicating if the string is sorted or not.

Here’s an example of how your function should behave. (Recall that the order operators are case-sensitive, so that "A" < "a" evaluates to True.)

is_sorted("ABC") == True
is_sorted("aBc") == False
is_sorted("dog") == False
"""

def is_sorted(string):
    """Returns True if string is sorted from least to greatest
       False otherwise.
    """
    # TODO: Fill in details
    last_letter = string[0]
    sort_flag = True
    for char in string:
        if char >= last_letter:
            last_letter = char
        else:
            sort_flag = False
            break
            
    return sort_flag

print(is_sorted("ABC"))
print(is_sorted("aBc"))
print(is_sorted("dog"))

"""
Bonus 1

Write a function that takes a sentence with an introductory prepositional phrase and returns the number of characters (including whitespace and punctuation) remaining in the string after the comma. For example, “Before you go to bed, you need to brush your teeth.” returns 30 and “Under the warm sun, the cat slept deeply.” returns 22.
"""
def char_count(phrase):
    index = phrase.find(",")
    new_str = phrase[index+1:]
    count = 0
    for char in new_str:
        count += 1
    return count

print(char_count("Before you go to bed, you need to brush your teeth."))

"""
Bonus 2

Write a function that takes in a string and converts that string to pig latin. Pig latin involves moving the first letter of a word to the end, then appending “ay.” For example, the phrase “python code wins” would turn into “ythonpay odecay insway.”

For an extra challenge, handle the case where a word starts with a vowel. In this case, the word should be unmodified except for adding “ay” at the end. For example, “all open androids” would become “allay openay androidsay.”
"""
def pig_latin(phrase):
    words = phrase.split()
    pig_words = []
    for word in words:
        word = list(word)
        char = word.pop(0)
        word.append(char + "ay")
        word = "".join(word)
        print(word)
        pig_words += [word]
        
    print(pig_words)
    return (" ".join(pig_words))

print("\n", (pig_latin("python code wins")) == "ythonpay odecay insway")