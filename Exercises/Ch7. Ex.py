"""4. Fill out the main function below so that you handle two exceptions that may be raised by your call to some_function. If this function raises a ValueError, print “value error happening now”; if this function raises a UnicodeError, print “unicode error happening now”. Make sure your code can handle both errors. (Note: since some_function isn’t filled out, neither exception will be raised when you run the program.)"""
def some_function():
    # Imagine code that could raise value or unicode errors
    pass

def main():
    # Put your exception handling code below
    try:
        some_function()
    except ValueError:
        print("value error happening now")
    except UnicodeError:
        print("unicode error happening now")

if __name__ == "__main__":
    main()

"""5. Write a function line(n) that returns a line with exactly n hashes.

Example:

    print(line(5))
Output:

    #####
"""
def line(n):
    str = ""
    
    for i in range(n):
        str += "#"
        
    return str

def main():
    print(line(5))
    print(line(7))
    
if __name__ == "__main__":
    main()

"""6. Write a function square(n) that returns an n by n square of hashes. Utilize your line function.

Example:

    print(square(5))

Output:

#####
#####
#####
#####
#####
"""
def line(n):
    str = ""
    
    for i in range(n):
        str += "#"
        
    return str

def square(n):
    for i in range(n):
        print(line(n))
        
def main():
    square(3)
    print("\n")
    square(5)
    
if __name__ == "__main__":
    main()

"""7. Write a function rectangle(width, height) that returns a rectangle of the width and height given by the parameters. Again, utilize your line function to do this.

Example:

    print(rectangle(5, 3))

Output:

#####
#####
#####
"""
def line(n):
    str = ""
    
    for i in range(n):
        str += "#"
        
    return str

def rectangle(width, height):
    for i in range(height):
        print(line(width))
        
def main():
    rectangle(5, 3)
    
    
if __name__ == "__main__":
    main()

"""8. Write a function stairs(n) that prints the pattern shown below, with height n. Again, utilize your line function to do this.

Example:

    stairs(5))

Output:

#
##
###
####
#####
"""
def line(n):
    str = ""
    
    for i in range(n):
        str += "#"
        
    return str

def stairs(n):
    for i in range(1, n+1):
        print(line(i))
        
def main():
    stairs(5)
    
    
if __name__ == "__main__":
    main()

"""9. Write a function space_line(spaces, hashes) that returns a line with exactly the specified number of spaces, followed by the specified number of hashes.

Example:

    print(space_line(3,5))

Output:

#This is where the edge is, so there's 3 spaces before hashes
   #####
"""
def line(n):
    str = ""
    
    for i in range(n):
        str += "#"
        
    return str

def space_line(spaces, hashes):
    str1 = ""
    str2 = line(hashes)
    
    for i in range(spaces):
        str1 += " "
        
    str = str1 + str2
    
    print("#This is where the edge is, so there's", spaces, 
          "spaces before hashes")
    print(str)
        
def main():
    space_line(3, 5)
    print("\n")
    space_line(5, 7)
    
    
if __name__ == "__main__":
    main()

"""10. Write a function triangle(n) that returns an upright triangle of height n.

Example:

    print(triangle(5))

Output:

    #
   ###
  #####
 #######
#########
"""
def line(n):
    str = ""
    
    for i in range(n):
        str += "#"
        
    return str

def space_line(spaces, hashes):
    str1 = ""
    str2 = line(hashes)
    
    for i in range(spaces):
        str1 += " "
        
    str = str1 + str2
    
    print(str)
        
def triangle(n):
    j = 1
    for i in range(1, n+1):
        space_line(n-i, j)
        j += 2
        
def main():
    triangle(5)
    
    
if __name__ == "__main__":
    main()

"""11. Write a function diamond(n) that returns a diamond where the triangle formed by the top portion has height n. Notice that this means the diamond has 2n - 1 rows.

Example:

    diamond(5))

Output:

    #
   ###
  #####
 #######
#########
 #######
  #####
   ###
    #
"""
def line(n):
    str = ""
    
    for i in range(n):
        str += "#"
        
    return str

def space_line(spaces, hashes):
    str1 = ""
    str2 = line(hashes)
    
    for i in range(spaces):
        str1 += " "
        
    str = str1 + str2
    
    print(str)
        
def diamond(n):
    j = 1
    k = 1
    for i in range(1, 2*n):
        space_line(n-k, j)
        if(i < n):
            j += 2
            k += 1
        else:
            j -= 2
            k -= 1
        
def main():
    diamond(5)
    
    
if __name__ == "__main__":
    main()

