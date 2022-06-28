print("Welcome to quize game")
name = input("Enter your name: ")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("get ready to start ...")


questions = ['What does the CPU stand for? ', 
'what is the first high level programming language? ', 
'what is the name that alan turing called the first computer design with? ',
'what is the nationality of alan turing? ',
'what is the years of 11-9 happend? ',
'who is the firs female programmer? ',
'how many continents in the world? ',
'which country coded by PA?',
]

answers = [
    'central processing unit',
    'fortran',
    'christopher',
    'british',
    '2001',
    'ada',
    '7',
    'palestine'
]

player_answer = []
answers_check = []
score = 0 

for i in range(len(questions)):
    print(questions[i]+" ")
    player_input = input()
    player_answer.append(player_input)
    if player_input.lower() != answers[i]:
        answers_check.append('False')
    else:
        answers_check.append('True')
        score += 1
    
print(f"your score is {score} out of {len(questions)}")
print('Question number || Question answer || your answer || if your get it correct')

for i in range(len(questions)):
    print(f'{i+1} \t {questions[i]} \t {answers[i]} \t {player_input[i]} \t {answers_check[i]}')
