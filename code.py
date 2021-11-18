import random;

def guessing_computer(x):
    low = 1;
    high = x;
    userAns = "";
    
    while userAns != "c":
        guess = random.randint(low,high);
        userAns = input(f"Is {guess} low(l), high(h) or correct(c)").lower();
        if userAns == "l" or userAns == "h" or userAns == "c":
            if userAns == "l":
                low = guess+1;
            elif userAns == "h":
                high = guess-1;
            else:
                print(f"\n The number is {guess}.\n Yay, Computer guessed it correctly.")
        else:
            print("Invalid input!, please try again.");
            
guessing_computer(100);
