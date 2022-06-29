from datetime import datetime

pwd = input ('What is the master Password?  ')


def view():
    with open('passwords.txt', 'r') as f:
        for r in f.readlines():
            print(r.rstrip())
    

def add():
    name = input('account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(f'name: {name} \t password: {pwd} \t added time: {datetime.now().strftime("%H:%M:%S")} \n')

while True:
    mod = input('would you like to add a new password of view existing ones (view/ add/ q- to quit)')

    if mod == 'q':
        break

    if mod == 'view':
        view()
    elif mod == 'add':
        add()
