import random
import string
from words import words

#hangman game
# x : number of attempts allowed
def hangman0(x):
    print(f"HANGMAN\nRULES : Guess the word in less than {x} attempts by suggesting a letter each round. Words to guess are in french.")
    #chose a word to guess
    word = random.choice(words).upper()
    wordGuessed = ""
    for i in range(len(word)):
        wordGuessed += "_ "
        
    lettersUsed =""
    nbError = 0
    wordSize = len(word)
    res = ""
    while nbError != x and res != word :
        print(wordGuessed)
        print(f"Letters suggested are : {lettersUsed}")
        
        #user guess
        letter = input("Suggest a letter : ").upper()
        while letter in lettersUsed or not IsLetter(letter):
            letter = input("You already guessed that letter. Suggest a letter : ").upper()
        while not IsLetter(letter):
            letter = input("You didn't type a valid character. Suggest a letter : ").upper()
        lettersUsed += letter
        
        #is letter in word
        foundLetter = False
        for i in range(wordSize) :
            if word[i] == letter :
                foundLetter = True
                l = list(wordGuessed)
                l[2*i] = letter
                wordGuessed =''.join(l)
        
        #delete spaces
        l = list(wordGuessed)
        l = [i for i in l if i != ' ']
        res = ''.join(l)
        
        if not foundLetter:
            nbError += 1
    
    if nbError == x :
        print(f"You lose. The word was {word}")
    else:
        print(f"You won ! The word was {word}")
        
###hangman

def hangman(x):
    print(f"HANGMAN\nRULES : Guess the word in less than {x} attempts by suggesting a letter each round. Words to guess are in french.")
    #chose a word to guess
    word = random.choice(words).upper()
    #print(word)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()
    guesses = 0
    
    while(len(word_letters) != 0 and guesses <= x ):
    
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(' '.join(word_list))
        print('Letters suggested are : '+' '.join(used_letters))
        user_letter = input('Suggest a letter: ').upper()
        
        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters :
                word_letters.remove(user_letter)
            else:
                guesses += 1
        elif user_letter in used_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character.")
     
    if len(word_letters) == 0 :
        print(f'You won! The word was {word}')
    else :
        print(f'You lost. The word was {word}')
    
###hangman
def isLetter(c):
    #only plain letters no accent
    return c >='A' and c <='Z'
###IsLetter

hangman(10)