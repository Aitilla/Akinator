import random
from pokemonDB import typeList


userPokemon = {}

#Maximum amount of Akinator questions 
allowedQuestions = 15

def getRandomType():
    return random.choice(typeList)

def typeGuess():
    for i in range(allowedQuestions):  
        pokemonType = getRandomType()  
        multiType = input('Does your Pokemon have more than one type?')
        if multiType == 'y':
            multiType = True
        else:
            print('\nYour Pokemon is only one type okay.')
            type1 = input('\n\nIs your pokemon', pokemonType+'?')
            print('\n')
        type1Guess = input('')
        if type1 == 'y':
            print('So your Pokemon is', pokemonType + '. Interesting.')
            type1 = pokemonType
        else:
            return typeGuess()
        

def intro():
    print('\nWelcome to "Akinator"')
    print('\nI will try to guess which pokemon you are thinking off based of some questions i will ask you')
    introChoice()

def introChoice():
    startQ = input('\nAre you ready to play?\nPress [y] then ENTER to play the game\n').lower
    if startQ == 'y':
        typeGuess()
    else:
        print('Incorrect input. Please try again')
        introChoice()

#Starts the game
if __name__ == "__main__":
    intro()
