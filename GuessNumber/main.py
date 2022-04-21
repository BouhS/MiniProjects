import random
import string

def guess(x):
    random_number = random.randint(1,x)
    nbTry = 0
    guessed_number = 0
    while(guessed_number != random_number):
        guessed_number = int(input(f"Guess a number between 1 and {x}: "))
        if (guessed_number < random_number):
            clue = "It's more. Guess again:"
        else:
            clue = "It's less. Guess again:"
        print(clue)
        nbTry += 1
    print(f"Congratulations! You've found number {random_number} in {nbTry} attempts !")

# computer guess a number picked by the user by taking user answers into account
def computer_guess(x):
    random_number = int(input(f"Number to guess between 1 and {x}:"))
    while(random_number > x or random_number < 1):
        random_number = int(input(f"Error. Please choose a number between 1 and {x}: "))
    
    guessed_number = 0
    answer = ""
    limit_lo = 1
    limit_hi = x
    nbTry = 0
    while(answer != "perfect"):
        #computer has to guess number
        guessed_number = random.randint(limit_lo,limit_hi)
        #user say if its less or more
        answer = input(f"Computer guessed {guessed_number}.Answer by typing \"perfect\", \"more\" or \"less\": ")
        if (answer.find("less") != -1):
            limit_hi = guessed_number - 1
        elif (answer.find("more") != -1):
            limit_lo = guessed_number + 1
        nbTry += 1
    print(f"Congratulations ! Computer guessed in {nbTry} attempts !")
    
def computer_smart_guess(x):
    random_number = int(input(f"Number to guess between 1 and {x}:"))
    while(random_number > x or random_number < 1):
        random_number = int(input(f"Error. Please choose a number between 1 and {x}: "))
    
    guessed_number = 0
    answer = ""
    limit_lo = 1
    limit_hi = x
    nbTry = 0
    while(answer != "perfect"):
        #computer guess median value
        guessed_number = limit_lo + (limit_hi - limit_lo) // 2
        #user say if its less or more
        answer = input(f"Computer guessed {guessed_number}.Answer by typing \"perfect\", \"more\" or \"less\": ")
        if (answer.find("less") != -1):
            limit_hi = guessed_number - 1
        elif (answer.find("more") != -1):
            limit_lo = guessed_number + 1
        nbTry += 1
    print(f"Congratulations ! Computer guessed in {nbTry} attempts !")    

n = 100
computer_smart_guess(n)