import turtle
import sys
sys.setExecutionLimit(70000)

def draw_square(t, size):
    for i in range(4): 
        t.forward(size)
        t.right(90)
    for i in range(4): 
        t.forward(size)
        t.left(90)
    for i in range(4): 
        t.backward(size)
        t.right(90)
    for i in range(4): 
        t.backward(size)
        t.left(90)
    
def draw_wheel(t, size, spokes):
    """draws a wheel"""
    
    angle = 360 / spokes
    
    for i in range(spokes):
        t.right(angle)
        draw_square(t, size)
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.speed(10)

draw_wheel(alex, 50, 20)

#Modify the square function given to you in section 5.4 of the textbook. Modify this function so that instead of computing the square, it can compute any positive integer exponent that is given to the function.
def mutiply(x, y):
    running_total = 0          # initialize the accumulator!
    
    for i in range(y):
        running_total = running_total + x

    return running_total

def exp(x, y):
    
    if y == 0:
        result = 1
    elif y == 1:
        result = x
    else:    
        num = x
        for i in range(y-1):
            result = mutiply(num, x)
            num = result
        
    return result

num = 3
power = 1
result = exp(num, power)
print("The result of", num, "to the power of", power, "is:", result)

"""

    The `Fibonacci sequence<https://en.wikipedia.org/wiki/Fibonacci_number>`_ is given as:

0, 1, 1, 2, 3, 5, 8, 13, 21...

Notice that each number in the series is simply the sum of the previous two numbers of the series. Write a function called fib(n) that takes in an integer n which is greater than 2 and returns the nth Fibonacci number. For example fib(4) would return 3, fib(6) would return 8 etc. (Hint: Remember that zero-based indexing we talked about...)

Note that it is tricky to compute fib(0) = 0 and fib(1) = 1 with the concepts we have currently covered. If you have done the prep work for chapter 6, however, you should be able to update your function to cover those two values.

Finally, investigate the following question: what is the largest value of n that returns the correct Fibonacci number? Why does this function stop working after that point?
"""
def fib(n):
    """compute the sum of the first n numbers in the Fibonacci sequence."""
    
    sum_fib = 0 
    prev_num = -1
    second_prev_num = -2
    curr_num =0
    seq = ""
    
    for i in range(n+1):
        if (second_prev_num < 0) or (prev_num < 0):
            second_prev_num = prev_num
            prev_num = curr_num
            curr_num = i
        else:
            second_prev_num = prev_num
            prev_num = curr_num
            curr_num = second_prev_num + prev_num
            
        sum_fib = sum_fib + curr_num
        seq = seq + str(curr_num) + ","
        
    #print("\nfib (", n, "):")
    #print("sequence is:", seq, "||", curr_num )          
    #print("sum is:", sum_fib)
    return curr_num
    
for i in range(10):
    num = fib(i)
    #print("fib({0}) is: {1}".format(i, fib(i)))
    print("\nfib (", i, ") is:", fib(i))
        
    