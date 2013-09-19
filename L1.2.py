import time
def displayIntro():
    print('Hi there! Who are you?')
    myName = input()
    print('Nice to meet you ,' + myName + '!')
    print('My name is... Well that\'s not important right now. What\'s important is that')
    print('I\'d like to aks you to join me in a little adventure...')
def letsStart():
    choice = ''
    while choice != 'y' or choice != 'n': 
        print('Do you feel up to it?')
        print('y or n')
        choice = input()
    return choice
def checkChoice(chosenChoice):
    goodChoice = 'y' 
    badChoice = 'n' 
    if chosenChoice == str(goodChoice):
        print('Well what are we waiting for? Let\'s go!')
    else:
        print('Oh... Too Bad you\'ll never now what it was about!')
              
playAgain = 'y'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    choiceMade = chooseChoice()
    checkChoice(choiceMade)          
    print('Would you like to change your mind?')
    playAgain = input()          
        
    
