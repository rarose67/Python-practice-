#2. Write a function that will return the number of digits in an integer.
def num_digits(integer):
    num = str(integer)
    return len(num)

print(num_digits(24565))

#3. Write a function that removes the first occurrence of a string from another string.
from test import testEqual

def remove(substr,original_string):
    # your code here
    new_str = ""
    found = False
    i = 0
    
    
    while i < len(original_string):
        #print("At the start of the loop, i is:", i, "and the string is:", new_str)
        if (original_string[i:i+len(substr)] == substr) and (found == False):
            i += len(substr)
            #print("yes")
            found = True
        else:
            new_str += original_string[i]
            #print("no")
            i += 1
        #print("At the end of the loop, i is:", i, "and the string is:", new_str)
            
    
    return new_str

testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')
testEqual(remove('oo', 'Yahoohoo'), 'Yahhoo')

#4. Write a function reverse that receives a string argument, and returns a reversed version of the string.
from test import testEqual

def reverse(text):
    # your code here
    new_str = ""
    
    for char in text:
        new_str = char + new_str
        
    return new_str
 
testEqual(reverse("happy"), "yppah")
testEqual(reverse("Python"), "nohtyP")
testEqual(reverse(""), "")

#5. Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!).
rom test import testEqual

def reverse(text):
    # your code here
    new_str = ""
    
    for char in text:
        new_str = char + new_str
        
    return new_str

def is_palindrome(text):
    if len(text) <= 1:
        return True
    else:
        middle = (len(text) // 2)
        first_str = text[:middle].strip()
        second_str = text[middle:].strip()
        
        #print(first_str)
        #print(second_str)
        #print(reverse(second_str), "\n")
        
        if(first_str == reverse(second_str)):
            return True
        else:
            return False
        

testEqual(is_palindrome('abba'), True)
testEqual(is_palindrome('abab'), False)
testEqual(is_palindrome('straw warts'), True)
testEqual(is_palindrome('a'), True)
testEqual(is_palindrome(''), True)

#6. Write a function that mirrors its argument. For example, mirror('good') should return a string holding the value gooddoog. (Hint: Make use of the reverse function).
def mirror(text):
    return(text+reverse(text))

def reverse(text):
    # your code here
    new_str = ""
    
    for char in text:
        new_str = char + new_str
        
    return new_str

from test import testEqual
testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')

"""7. Write a function that implements a substitution cipher. In a substitution cipher one letter is substituted for another to garble the message. For example A -> Q, B -> T, C -> G etc. your function should take two parameters, the message you want to encrypt, and a string that represents the mapping of the 26 letters in the alphabet. Your function should return a string that is the encrypted version of the message."""
def encypt(mess, cipher):
    # Your code here
    new_str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in mess:
        if(char == " "):
            new_str += char
        else:
            pos = alphabet.find(char)
            new_str += cipher[pos]
        
    return new_str

def main():
    print(encypt('abcde', 'BcDeFgHiJkLmNoPqRsTuVwXyZa'))
    print(encypt('nopqr', 'BcDeFgHiJkLmNoPqRsTuVwXyZa'))
    print(encypt(encypt('a', 'BcDeFgHiJkLmNoPqRsTuVwXyZa'), 'BcDeFgHiJkLmNoPqRsTuVwXyZa'))

if __name__ == "__main__":
    main()

"""8. Write a function that decrypts the message from the previous exercise. It should also take two parameters. The encrypted message, and the mixed up alphabet. The function should return a string that is the same as the original unencrypted message."""
def encypt(mess, cipher):
    # Your code here
    new_str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in mess:
        if(char == " "):
            new_str += char
        else:
            pos = alphabet.find(char)
            new_str += cipher[pos]
        
    return new_str

def decypt(mess, cipher):
    # Your code here
    new_str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in mess:
        if(char == " "):
            new_str += char
        else:
            pos = cipher.find(char)
            new_str += alphabet[pos]
        
    return new_str

def main():
    print(encypt('abcde', 'BcDeFgHiJkLmNoPqRsTuVwXyZa'))
    print(decypt('nopqr', 'BcDeFgHiJkLmNoPqRsTuVwXyZa'))
    print(decypt(encypt('abcde', 'BcDeFgHiJkLmNoPqRsTuVwXyZa'), 'BcDeFgHiJkLmNoPqRsTuVwXyZa'))

if __name__ == "__main__":
    main()

"""9. Write a function called rot13 that uses the Caesar cipher to encrypt a message. The Caesar cipher works like a substitution cipher but each character is replaced by the character 13 characters to “its right” in the alphabet. So for example the letter “a” becomes the letter “n”. If a letter is past the middle of the alphabet then the counting wraps around to the letter “a” again, so “n” becomes “a”, “o” becomes “b” and so on. Hint: Whenever you talk about things wrapping around its a good idea to think of modulo arithmetic (using the remainder operator)."""
def rot13(mess):
    # Your code here
    new_str = ""
    for char in mess:
        if(char == " "):
            new_str += char
        else:
            num = ord(char)
            num += 13

            if (num // ord("z") > 0):
                num = ord("a") + (num % ord("z")) - 1
                
            new_str += chr(num)
        
    return new_str

def main():
    print(rot13('abcde'))
    print(rot13('nopqr'))
    print(rot13(rot13('since rot thirteen is symmetric you should see this message')))
    print(rot13(rot13('a')))

if __name__ == "__main__":
    main()


"""Weekly Graded Assignment

Write a function analyze_text that receives a string as input. Your function should count the number of alphabetic characters (a through z, or A through Z) in the text and also keep track of how many are the letter 'e' (upper or lowercase).

Your function should return an analysis of the text in the form of a string phrased exactly like this:

“The text contains 240 alphabetic characters, of which 105 (43.75%) are ‘e’.”

You will need to make use of the isalpha function, which can be used like this

"a".isalpha() # => evaluates to True
"3".isalpha() # => evaluates to False
"&".isalpha() # => False
" ".isalpha() # => False

mystr = "Q"
mystr.isalpha() # => True
"""

def analyze_text(text):
    """count the number of alphabetic characters (a through z, or A through Z) in the text and also keep track of 
    how many are the letter 'e' (upper or lowercase)."""
    
    #initialize accumulators
    e_count = 0
    letter_count = 0
    
    for char in text:
        if (char.isalpha()):   #if the current character is an alphabetic character, increase the counter.
            letter_count += 1 
            if ((char == "E") or (char == "e")):  #if the current character is 'e' or 'E', increase the counter.
                e_count += 1
    
    #Initialize the analysis string, with placeholders the variables.
    analysis = "The text contains {0} alphabetic characters, of which {1} ({2}%) are 'e'."
    
    #return the formatted analysis string
    return(analysis.format(letter_count, e_count, ((e_count / letter_count) * 100)))


# Don't copy these tests into Vocareum!
# Note that depending on whether you use str.format or string concatenation
# your code will pass different tests. As long as your code passes either
# tests 1-3 OR tests 4-6, it should pass in Vocareum. See below for more details.
from test import testEqual

# Tests 1-3: solutions using string concatenation should pass these
text1 = "Eeeee"
answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(text1), answer1)

text2 = "Blueberries are tasteee!"
answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
testEqual(analyze_text(text2), answer2)

text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(text3), answer3)

# Tests 4-6: solutions using str.format should pass these
text4 = "Eeeee"
answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."
testEqual(analyze_text(text4), answer4)

text5 = "Blueberries are tasteee!"
answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
testEqual(analyze_text(text5), answer5)

text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."
testEqual(analyze_text(text6), answer6)
