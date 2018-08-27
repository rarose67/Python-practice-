#For this studio, your job is to write an algorithm that processes an image to make it “fuzzy” looking:
"""The algorithm to achieve this effect is actually fairly simple: for each pixel, randomly choose one of its neighboring pixels, and use that pixel’s color instead.

For example, imagine that the table below is a zoomed-in view of the pixels in our image, and that we are trying to alter the center pixel (the one whose color is E):

A  B  C
D  E  F
G  H  I

We want to randomly choose one of the 9 pixels in this grid, and insert its color to replace the center one. Let’s say we choose the bottom-left. This will alter the resulting image like so:

A  B  C
D  G  F
G  H  I

Notice that the center pixel received the color G.

Of course, you want to run every pixel through this same process, so the outer ones should change as well (but in the example above, we only focused on the particular moment when the center pixel was being altered).

Also note that it is okay if, when randomly selecting a neighbor, you happen to choose the center pixel itself. The resulting pixel will be unchanged, but this should happen rarely enough (once per 9 tries) that the overall image will still be nice and fuzzy. Not worrying about this fluke will shorten the amount of code you need to write.
Tips

    If you use pixel indexes i and j, you can access the neighbors by adding and subtracting one from those numbers, i.e. i+1, i-1, ...
    If your pixel is on the very edge of the image, then you won’t have 8 neighbors to choose from. For example, on the left edge, you don’t have any neighbors to your left. Lucky for you, we’ve given you starter code in which the iteration starts at 1 instead of 0, and stops 1 pixel short of the max. You’re welcome!

"""

import image
import sys
import random

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        try:
            # TODO: Randomly choose the coordinates of a neighboring pixel 
            row = random.randrange(j-1, j+1)
            col = random.randrange(i-1, i+1)
        
            p = img.getPixel(col, row)
        
            new_red = p.getRed()
            new_green = p.getGreen()
            new_blue = p.getBlue()
        
            new_pixel = image.Pixel(new_red, new_green, new_blue)

            # TODO: in the new image, set this pixel's color to the neighbor's color
            new_img.setPixel(i, j, new_pixel)
        except ValueError:
            continue

new_img.draw(win)
win.exitonclick()

"""
Bonus 1

Write a function that takes in an integer and then displays the multiplication table of that size. For example, if the given integer was 3, the following multiplication table would be displayed:

0 0 0 0
0 1 2 3
0 2 4 6
0 3 6 9
"""
def multi_table(num):
    for i in range(num + 1):
        row = ""
        for j in range(num + 1):
            row += str(i*j) + " "
        print(row)
        
multi_table(3)

"""
Bonus 2

Write a program that allows someone to play the classic game of rock, paper, scissors against the computer. First, prompt the user to enter how many games should be played in a “best of” format, i.e. best of 5 would require someone to win 3 times, best of 9 would require someone to win 5 times, etc.

Next, start to simulate the games. For the human player, you should prompt them to enter whether they would like to play rock, paper, or scissors. The computer player should randomly choose one of the three options. You should then display the result of the match and current number of wins for each player. If a tie occurs, it should not count towards the total number of matches played.

Hint

Hint: it may be easier to use numbers to represent the three different choices of “rock”, “paper”, and “scissors.”
"""
import random

def rock_paper_scissors():
    sign_p1 = random.randrange(1, 3)
    sign_com = random.randrange(1, 3)
    
    if((sign_p1 == 1) and (sign_com == 3)):
        print("The player wins")
        return 1
    elif (sign_p1 > sign_com):
        print("The player wins")
        return 1
    elif (sign_p1 == sign_com):
        print("It's a tie")
        return 0
    else:
        print("The computer won")
        return -1
    
def best_of(num):
    num_wins = 0
    num_games = 0
    num_losses = 0
    
    while num_games <= num:
        if (rock_paper_scissors() == 1):
            num_wins += 1
            num_games += 1
        elif (rock_paper_scissors() == -1):
            num_losses += 1
            num_games += 1    
            
        if(num_wins > (num // 2)) or (num_losses > (num // 2)):
            break
            
    print("You won", num_wins, "games out of", num)
    print("the computer won", num_losses, "games out of", num, "\n")
    
    if(num_wins > (num // 2)):
        print("You won!")
    elif (num_losses > (num // 2)):
        print("the computer won")
    
best_of(7)
    
            