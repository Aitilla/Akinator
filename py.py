

def startGame():
    q1 = input('\n\nAre you Male?')

def intro():
    print('\nWelcome to "Akinator"')
    print('\nI will try to guess who you are thinking off based of some questions i will ask you')
    introChoice()

def introChoice():
    startQ = input('\nAre you ready to play?\nPress [y] then ENTER to play the game\n').lower
    
    if startQ == 'y':
        startGame()

#Starts the game
if __name__ == "__main__":
    intro()

print('hello world')