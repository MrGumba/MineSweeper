# coding: utf-8

def menu(hardness = 1):
    errorText = 'Du skrev inte in ett heltal mellan dom tillåtna värderna '
    print('--------------')
    print('Start       (1)')
    print('Difficulty  (2)')
    print('Exit        (3)')
    while True:
        try:
            menuSelect = int(input('Skriv in vilket meny alternativ du vill välja (1, 2, eller 3): '))
            if menuSelect == 1:
                mineSweeper()
            elif menuSelect == 2:
                difficulty()
            elif menuSelect == 3:
                return            
            break
        except ValueError:
            print(errorText)      

def mineSweeper(hardness = 1):
    mapMaker(hardness)

def difficulty():
    print('easy (1)')
    while True:
        try:
            difficultySelect = int(input('Välj en av svårighets graderna genom att skriva (1): '))
            if difficultySelect > 0 and difficultySelect < 2:
                break
        except ValueError:
            print(errorText)
    menu(difficultySelect)
        
def mapMaker(hardness):
    

menu()