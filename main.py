import random


#RULES
'''
Rock beat Scissors
Scissors beat Paper
Paper beat Rock
'''

while True:
    options = ['Rock', 'Scissors', 'Paper']
    computer = random.choice(options)
    player = None
    
    while player not in options:
        print("Invalid Option")
        pass
        player = input("Enter an option -- Rock, Scissors or Paper: ")
           
    if player == computer:
        print(f"Computer ({computer}) : player ({player})")
        print('Tie, Play again')
        player = input("Enter an option -- Rock, Scissors or Paper: ")

    elif player == 'Rock' and computer == 'Scissors' or player =='Scissors' and computer == 'Paper' or player == 'Paper' and computer == 'Rock':
        print(f"Player ({player}) : CPU ({computer})")
        print("You win")
        break
    
    elif player == 'Scissors' and computer == 'Rock' or player =='Paper' and computer == 'Scissors' or player == 'Rock' and computer == 'Paper':
        print(f" Player ({player}) : CPU ({computer})")
        print("Computer win")
        break




        

