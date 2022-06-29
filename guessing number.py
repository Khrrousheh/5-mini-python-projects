import random

print("this game is called gussing the number you have in total range 10 number to gussing between")


start_range = int(input('input the start range '))
mynumber = random.randrange(start_range, start_range + 11)

attempt = 2
win = False
while attempt >= 0:
    player_input = int(input())
    if player_input == mynumber:
        win = True
        break
    elif player_input > mynumber:
        print('try lower number')
    else:
        print('try higher number')
    attempt -= 1

if win:
    print('congratulation you guess the number')
else:
    print(f"you did a great work unfortunalty my number was {mynumber} and you didn't gusse it")