"""
For this studio, we are going to hone our detective skills by finding and fixing the bugs in the following program.

    Sherlock Holmes, in one of his famous “black moods”, has locked himself in his Baker Street flat. There are only two people on his list of who may enter, Dr. Watson and Inspector Lestrade. Everyone else he wants to send away.

We’ve written a program to reflect his wishes, but the code doesn’t seem to work at all. In fact, it’s a hot mess of errors!

Work through the code to debug all the errors. You have the error messages and your knowledge of coding “right and wrong” to guide you. You might want to look for obvious errors first and fix those; then proceed to fix the remaining errors by looking at the exceptions you get. But follow whatever process you think best. We’ll give you one clue to start: only the sherlock function code has errors; the rest of the program is correct.

In the end, running this program — with the code included in main — should yield these results:

Go Away! (sound of violin music...)
Go Away! (sound of violin music...)
Go Away! (sound of violin music...)
Go Away! (sound of violin music...)
Enter
"""

def sherlock(guests):
    let_in = True
    for guest in guests:
        if (guest == "Dr. Watson") or (guest == "Inspector Lestrade"):
            let_in = True
        else:
            let_in = False
            break
            
    if let_in:
        return "Enter"
    else:
        return "Go Away! (sound of violin music...)"

def main():
    press = ["a reporter from the Times", "a reporter from the Observer"]
    family_etc = ["Mycroft Holmes", "Mrs. Hudson"]
    enemies = ["Professor Moriarty", "Charles Augustus Milverton", "John Woodley"]
    potential_love_interest = ["Irene Adler"]
    friends = ["Inspector Lestrade", "Dr. Watson"]
    print(sherlock(press))
    print(sherlock(family_etc))
    print(sherlock(enemies))
    print(sherlock(potential_love_interest))
    print(sherlock(friends))

if __name__ == "__main__":
    main()
