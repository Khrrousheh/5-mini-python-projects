import random


print('welcome to Rock, Paper, Scissors game')

play_again = True

option = ['rock','paper', 'Scissors']

while play_again:
    myotion = random.randrange(len(option))
    player_input= int(input("input only number\n [0] Rock [1] Paper [2] Scissors \n[3] to end the game "))
    if player_input == 3:
        quit()
    print(f'you chose {option[player_input]} and i chose {option[myotion]}')

    if myotion == player_input: 
        print('Draw')
    elif option[myotion] == 'rock' and option[player_input] == 'paper':
        print('You win')
    elif option[myotion] == 'rock' and option[player_input] == 'Scissors':
        print('I win')
    elif option[myotion] == 'paper' and option[player_input] == 'Scissors':
        print('you win')
    elif option[myotion] == 'paper' and option[player_input] == 'rock':
        print('I win')
    elif option[myotion] == 'Scissors' and option[player_input] == 'rock':
        print('You win')
    elif option[myotion] == 'Scissors' and option[player_input] == 'paper':
        print('I win')
    
    # c = input('Do you want to quit? ')
    # if c.lower != 'yes':
    #     play_again =False
