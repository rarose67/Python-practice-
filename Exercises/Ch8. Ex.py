"""1. Write a function print_triangular_numbers(n) that prints out the first n triangular numbers. A call to print_triangular_numbers(5) would produce the following output:

1
3
6
10
15

(Hint: use a web search to find out what a triangular number is.)"""
def print_triangular_numbers(n):
    """print the triangular numbers from 1 to n"""
    
    for i in range(1, n+1):
        num = (i * (i + 1)) / 2
        print(int(num))
        
print_triangular_numbers(5)

#2. Modify the walking turtle program so that rather than a 90 degree left or right turn the angle of the turn is determined randomly at each step.
import random
import turtle

def is_in_screen(screen, t):
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False

    return still_in

def main():
    julia = turtle.Turtle()
    screen = turtle.Screen()

    julia.shape('turtle')
    while is_in_screen(screen, julia):
        coin = random.randrange(0, 2)
        angle = random.randrange(0, 360)
        if coin == 0:
            julia.left(angle)
        else:
            julia.right(angle)

        julia.forward(50)

    screen.exitonclick()

if __name__ == "__main__":
    main()

#3. Modify the turtle walk program so that you have two turtles each with a random starting location. Keep the turtles moving until one of them leaves the screen.
import random
import turtle
import sys
sys.setExecutionLimit(70000)

def is_in_screen(screen, t):
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False

    return still_in

def main():
    screen = turtle.Screen()
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    jx_start = random.randrange(left_bound, right_bound)
    jy_start = random.randrange(bottom_bound, top_bound)
    ax_start = random.randrange(left_bound, right_bound)
    ay_start = random.randrange(bottom_bound, top_bound)
    
    julia = turtle.Turtle()
    alex = turtle.Turtle()
    
    julia.goto(jx_start, jy_start)
    alex.goto(ax_start, ay_start)

    julia.shape('turtle')
    alex.shape('turtle')
    while (is_in_screen(screen, julia)) and (is_in_screen(screen, alex)):
        coin = random.randrange(0, 2)
        angle = random.randrange(0, 360)
        if coin == 0:
            julia.left(angle)
        else:
            julia.right(angle)

        julia.forward(50)
        
        coin = random.randrange(0, 2)
        angle = random.randrange(0, 360)
        if coin == 0:
            alex.left(angle)
        else:
            alex.right(angle)

        alex.forward(50)


    screen.exitonclick()

if __name__ == "__main__":
    main()

#4. Modify the previous turtle walk program so that the turtle turns around when it hits the wall or when one turtle collides with another turtle.
import random
import turtle
import sys
sys.setExecutionLimit(70000)

def is_in_screen(screen, t):
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
        turn_around(t)
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False
        turn_around(t)

    return still_in

def intersect(t1_x1, t1_y1, t1_x2, t1_y2, t2_x1, t2_y1, t2_x2, t2_y2):
    
    if(t1_x1 == t1_x2) and (t2_x1 == t2_x2):
        print("The lines don't intersect.")
    elif (t1_x1 == t1_x2):
        t2_slope = (t2_y2 - t2_y1) / (t2_x2 - t2_x1)
        b2 = -(t2_slope * t2_x1) + t2_y1
        x_intersect = t1_x1
        y_intersect = (t2_slope * x_intersect) + b2
    elif (t2_x1 == t2_x2):
        t1_slope = (t1_y2 - t1_y1) / (t1_x2 - t1_x1)
        b1 = -(t1_slope * t1_x1) + t1_y1
        x_intersect = t2_x1
        y_intersect = (t1_slope * x_intersect) + b1
    else:
        t1_slope = (t1_y2 - t1_y1) / (t1_x2 - t1_x1)
        t2_slope = (t2_y2 - t2_y1) / (t2_x2 - t2_x1)
    
        b1 = -(t1_slope * t1_x1) + t1_y1
        b2 = -(t2_slope * t2_x1) + t2_y1
        x_intersect =  (b1 - b2) / (t1_slope - t2_slope)
        y_intersect = (t1_slope * x_intersect) + b1
    
    print("X: ", x_intersect, "Y: ", y_intersect)   
    
    x1_range = ((t1_x1 <= x_intersect) and (x_intersect <= t1_x2)) 
    x2_range = ((t2_x1 <= x_intersect) and (x_intersect <= t2_x2)) 
    y1_range = ((t1_y1 <= y_intersect) and (y_intersect <= t1_y2)) 
    y2_range = ((t2_y1 <= y_intersect) and (y_intersect <= t2_y2))
    
    if(x1_range and x2_range and y1_range and y2_range):
        print("The lines intersect.")
    else:
        print("The lines don't intersect.")
    
    
def move(t1, t2, distance1 distance2):
    turtle1_x1 = t1.xcor()
    turtle1_y1 = t1.ycor()
    turtle2_x1 = t2.xcor()
    turtle2_y1 = t2.ycor()
    
    t1.up()
    t2.up()i
    t1.forward(distance1)
    t2.forward(distance2)
    turtle1_x2 = t1.xcor()
    turtle1_y2 = t1.ycor()
    turtle2_x2 = t2.xcor()
    turtle2_y2 = t2.ycor()
    t1.backward(distance1)
    t2.backward(distance2)
    t1.down()
    t2.down()
    
    if(intersect(turtle1_x1, turtle1_y1, turtle1_x2, turtle1_y2, turtle2_x1, turtle2_y1, turtle2_x2, turtle2_y2)):
        
    
def turn_around(t):
    turtle_x = t.xcor()
    turtle_y = t.ycor()

    t.left(180)
    t.forward(50)
    
    print("turn around,  ", turtle_x, " ", turtle_y)
    
def main():
    screen = turtle.Screen()
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    jx_start = random.randrange(left_bound, right_bound)
    jy_start = random.randrange(bottom_bound, top_bound)
    ax_start = random.randrange(left_bound, right_bound)
    ay_start = random.randrange(bottom_bound, top_bound)
    
    julia = turtle.Turtle()
    alex = turtle.Turtle()
    
    julia.goto(jx_start, jy_start)
    alex.goto(ax_start, ay_start)

    julia.shape('turtle')
    alex.shape('turtle')
    while (is_in_screen(screen, julia)) or (is_in_screen(screen, alex)):
        coin = random.randrange(0, 2)
        angle = random.randrange(0, 360)
        if coin == 0:
            julia.left(angle)
        else:
            julia.right(angle)

        julia.forward(50)
        
        coin = random.randrange(0, 2)
        angle = random.randrange(0, 360)
        if coin == 0:
            alex.left(angle)
        else:
            alex.right(angle)

        alex.forward(50)


    screen.exitonclick()

if __name__ == "__main__":
    main()

"""5. Here’s the start of a program for a weight training app that coaches users on how much weight they should lift for each of these three lifts: squat, bench, and deadlift. The program begins by having the user lift only 10 pounds for each lift. Each time they complete a set for a particular lift and say they are ready for the next set, add 10 pounds to the weight of their previous set and print a message that this is the new weight they should lift. The sets are all done for one lift at a time. So, for example, a user might squat 10 pounds, then 20 pounds, then 30 pounds and then say they don’t want to keep doing that lift. In this case, they’ll now get a printed message to bench 10 pounds, and so on and so forth.

Some of the code is already included below, but you will need to fill in the rest of the main function to produce the following functionality:

    For each lift, beginning with the squat, the function workout_coach should be called with the name of the lift and the current weight. This function prints a message to the user like the following:

    Time to squat 10 pounds! You got this!

    Keep calling workout_coach for as long as the user answers “yes” to the following question: “Keep doing the squat? Enter yes for the next set.” (Note that you will need to fill in the name of the lift depending on which lift in the iteration they are on.) You can do something like the following to combine strings and a variable to create the prompt string:

input_prompt = "Keep doing the " + lift + "? Enter yes for the next set."

    If the user answers with anything besides “yes” to the above question, then stop calling workout_coach for that particular lift and move on to repeat the above process for the next lift (unless it is the deadlift, which is the last lift and thus once the user decides to stop at this point the program quits).
    There is one special case where you should stop calling workout_coach — no matter what the user responds — and that is when the current weight is greater than 200 pounds for the bench. You have not yet talked with a lawyer about your app and you don’t want to get sued if anyone has a mishap, so you’re not going to encourage them to lift more than that amount of weight on the bench press (which is the exercise that, done improperly and without a spotter, causes most gym accidents). It is okay to keep encouraging users to lift more than 200 pounds for the squat and the deadlift, though, so you don’t need to set an upper limit for those lifts.

Here is some example output from a program run:

Time to squat 10 pounds! You got this!
Time to squat 20 pounds! You got this!
Time to bench 10 pounds! You got this!
Time to bench 20 pounds! You got this!
Time to bench 30 pounds! You got this!
Time to deadlift 10 pounds! You got this!
Time to deadlift 20 pounds! You got this!
Time to deadlift 30 pounds! You got this!
Time to deadlift 40 pounds! You got this!

"""
import sys

def workout_coach(lift_name, wt):
    print("Time to", lift_name, wt, "pounds! You got this!")

def main():
    sys.setExecutionLimit(120000) # keep program from timing out
    lifts = ["squat", "bench", "deadlift"]
    # Your code here
    for lift in lifts:
        weight = 10
        stop = False
        
        while(stop == False):
            workout_coach(lift, weight)
            ans = input("Keep doing the " + lift + "? Enter yes for the next set.")
            if((ans != "yes") and (ans != "Yes")):
                stop = True
            else:
                weight += 10
                
            if((weight > 200) and (lift == "bench")):
                stop = True

if __name__ == "__main__":
    main()

#6. Write a program to remove all the red from an image.
import image
import sys
sys.setExecutionLimit(70000)

img = image.Image("image.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)    # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
                     
        green = p.getGreen()
        blue = p.getBlue()
        
        new_pixel = image.Pixel(0, green, blue)
        
        img.setPixel(col, row, new_pixel)
        
img.draw(win)
win.exitonclick()

#7. Write a function to convert the image to grayscale.
import image
import sys
sys.setExecutionLimit(70000)

img = image.Image("image.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)    # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
                     
        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        
        gray = (red + green + blue) / 3
        
        new_pixel = image.Pixel(gray, gray, gray)
        
        img.setPixel(col, row, new_pixel)
        
img.draw(win)
win.exitonclick()

#8. Write a function to convert an image to black and white.
import image
import sys
sys.setExecutionLimit(70000)

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)    # setDelay(0) turns off animation

black = 0
white = 255
for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
                     
        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        
        gray = (red + green + blue) / 3
        
        if (gray > 140):
            color = white
        else:
            color = black
        
        new_pixel = image.Pixel(color, color, color)
        
        img.setPixel(col, row, new_pixel)
        
img.draw(win)
win.exitonclick()

import image

def convert_black_white(input_image):
    grayscale_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())

    for col in range(input_image.getWidth()):
        for row in range(input_image.getHeight()):
            original_pixel = input_image.getPixel(col, row)

            red = original_pixel.getRed()
            green = original_pixel.getGreen()
            blue = original_pixel.getBlue()

            avg = (red + green + blue) / 3.0

            new_pixel = image.Pixel(avg, avg, avg)
            grayscale_image.setPixel(col, row, new_pixel)

    black_white_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())
    for col in range(input_image.getWidth()):
        for row in range(input_image.getHeight()):
            original_pixel = grayscale_image.getPixel(col, row)
            red = original_pixel.getRed()
            if red > 140:
                val = 255
            else:
                val = 0

            new_pixel = image.Pixel(val, val, val)
            black_white_image.setPixel(col, row, new_pixel)
    return black_white_image

def main():
    img = image.Image("luther.jpg")
    win = image.ImageWin(img.getWidth(), img.getHeight())

    bw_img = convert_black_white(img)
    bw_img.draw(win)

    win.exitonclick()

if __name__ == "__main__":
    main()

"""9. Sepia Tone images are those brownish colored images that may remind you of times past. The formula for creating a sepia tone is as follows:

new_r = (R × 0.393 + G × 0.769 + B × 0.189)
new_g = (R × 0.349 + G × 0.686 + B × 0.168)
new_b = (R × 0.272 + G × 0.534 + B × 0.131)

Write a function to convert an image to sepia tone. Hint: Remember that RGB values must be integers between 0 and 255."""
import image
import sys
sys.setExecutionLimit(70000)

def sepia_tone(input_image):
    st_image = image.EmptyImage(input_image.getWidth(), input_image.getHeight())
    for row in range(input_image.getHeight()):
        for col in range(input_image.getWidth()):
            p = input_image.getPixel(col, row)
                     
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
        
            new_r = int((red * 0.393 + green * 0.769 + blue * 0.189))
            new_g = int((red * 0.349 + green * 0.686 + blue * 0.168))
            new_b = int((red * 0.272 + green * 0.534 + blue * 0.131))
        
            new_pixel = image.Pixel(new_r, new_g, new_b)
        
            st_image.setPixel(col, row, new_pixel)
        
    return st_image
        
img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

st_image = sepia_tone(img)
st_image.draw(win)
win.exitonclick()

#10. Write a function to uniformly enlarge an image by a factor of 2 (in other words, make the image twice as wide and twice as tall).
import image
import sys
sys.setExecutionLimit(70000)

def enlarge_image(input_image):
    st_image = image.EmptyImage(input_image.getWidth()*2, input_image.getHeight()*2)
    for row in range(input_image.getHeight()):
        for col in range(input_image.getWidth()):
            p = input_image.getPixel(col, row)
                     
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
        
            new_pixel = image.Pixel(red, green, blue)
        
            st_image.setPixel(col*2, row*2, new_pixel)
            st_image.setPixel(col*2+1, row*2, new_pixel)
            st_image.setPixel(col*2, row*2+1, new_pixel)
            st_image.setPixel(col*2+1, row*2+1, new_pixel)
        
    return st_image
        
img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth()*2, img.getHeight()*2)
img.draw(win)

st_image = enlarge_image(img)
st_image.draw(win)
win.exitonclick()

"""11. After you have scaled an image too much it looks blocky. One way of reducing the blockiness of the image is to replace each pixel with the average values of the pixels around it. This has the effect of smoothing out the changes in color. Write a function that takes an image as a parameter and smooths the image. Your function should return a new image that is the same as the old one but smoothed."""
import image
import sys
sys.setExecutionLimit(70000)

def smooth_image(input_image):
    copy_image = image.EmptyImage(input_image.getWidth()+2, input_image.getHeight()+2)
    
    for row in range(input_image.getHeight()):
        for col in range(input_image.getWidth()):
            p = input_image.getPixel(col, row)
                     
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()
        
            new_pixel = image.Pixel(red, green, blue)
        
            copy_image.setPixel(col+1, row+1, new_pixel)
            
    print(copy_image.getWidth(), copy_image.getHeight())
    
    sm_image = image.EmptyImage(copy_image.getWidth(), copy_image.getHeight())
    
    for row in range(1, copy_image.getHeight()-1):
        for col in range(1, copy_image.getWidth()-1):
            try:
                p = input_image.getPixel(col, row)
                p_r = input_image.getPixel(col+1, row)
                p_u = input_image.getPixel(col, row-1)
                p_d = input_image.getPixel(col, row+1)
                p_l = input_image.getPixel(col-1, row)
                p_ru = input_image.getPixel(col+1, row-1)
                p_lu = input_image.getPixel(col-1, row-1)
                p_rd = input_image.getPixel(col+1, row+1)
                p_ld = input_image.getPixel(col-1, row+1)
                
                sm_red = int((p_r.getRed() + p_u.getRed() + p_ru.getRed() + p_l.getRed() + p_lu.getRed() +
                           p_d.getRed() + p_rd.getRed() + p_ld.getRed() + p.getRed()) / 9)
                sm_green = int((p_r.getGreen() + p_u.getGreen() + p_ru.getGreen() + p_l.getGreen() +
                             p_lu.getGreen()+ p_d.getGreen() + p_rd.getGreen() + p_ld.getGreen() +
                            p.getGreen()) / 9)
                sm_blue = int((p_r.getBlue() + p_u.getBlue() + p_ru.getBlue() + p_l.getBlue() + 
                            p_lu.getBlue() + p_d.getBlue() + p_rd.getBlue() + p_ld.getBlue() +
                            p.getBlue()) / 9)  
        
                sm_new_pixel = image.Pixel(sm_red, sm_green, sm_blue)
        
                st_image.setPixel(col, row, sm_new_pixel)
            
            except ValueError:
                #print("ValueError at Row:", row, " Col:", col)
                pass
    return sm_image
        
img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)

st_image = smooth_image(img)
st_image.draw(win)
win.exitonclick()


"""Weekly Graded Assignment

Write a course_grader function that takes a list of test scores as its parameter. It will add up these test scores and calculate an average score. It should then return a message of "pass" or "fail" depending on these two conditions:

    If the average score is greater than or equal to 70 and no single test score is below 50, then return a message of "pass".
    If the average score is lower than 70 or at least one test score is below 50, then return a message of "fail".

Some sample function calls with comments on what should be printed out are included in main for testing purposes. You should only put the code for the course_grader function into Vocareum.
"""

def course_grader(test_scores):
    # Your code here
    total_score = 0
    has_one_failed = False
       
    for score in test_scores:
        total_score += score "accumulator for scores
        if score < 50:  #if a score below 50 is found, end the loop because that is an automatic fail.
            has_one_failed = True
            break
        
    average_score = total_score / len(test_scores)
    
    if(average_score < 70.0) or (has_one_failed):
        return "fail"
    else:
        return "pass"

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()
