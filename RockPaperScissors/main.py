import random


#ROCK PAPER SCISSORS game
def isWinner(player, opponent):
    return (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R')

def playRockPaperScissors():
    #Explain the rules
    print('ROCK PAPER SCISSORS \nRules : Rock crushes Scissors. Paper covers Rock. Scissors cut Paper')
    
    choices = ['r','p','s'] #can also be ['R','P','S']
    # user pick rock paper or scissors
    user_pick = input('Choose between Rock(R), paper(P) and scissors(S) : ').lower()
    
    #check if user response is r, p or s if not output error
    if user_pick not in choices :
       return 'ERROR'
       
    # computer pick rock paper or scissors
    comp_pick = random.choice(choices)
    
    # who won ?
    if user_pick == comp_pick :
        return 'It\'s a tie'
        
    if isWinner(user_pick,comp_pick):
        return 'You won !'
    else :
        return 'Computer won'

#TODO : do ROCK PAPER SCISSORS LIZARD SPOCK 
def playRockPaperScissorsLizardSpock():
    #Explain the rules
    print('ROCK PAPER SCISSORS LIZARD SPOCK \nRules : Rock crushes Scissors. Paper covers Rock. Scissors cut Paper')

print(playRockPaperScissors())