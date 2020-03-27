import random

elements = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf',
            'sponge', 'paper', 'air', 'water', 'dragon', 'devil',
            'lightning', 'gun']
options = {'rock': elements[1:8],
           'fire': elements[2:9],
           'scissors': elements[3:10],
           'snake': elements[4:11],
           'human': elements[5:12],
           'tree': elements[6:13],
           'wolf': elements[7:14],
           'sponge': elements[8:15],
           'paper': elements[9::]+elements[:1],
           'air': elements[10::]+elements[:2],
           'water': elements[11::]+elements[:3],
           'dragon': elements[12::]+elements[:4],
           'devil': elements[13::]+elements[:5],
           'gun': elements[:7]}


def paṕer_win(p, u):
    if p == 'paper' and u == 'rock':
        return True
    return False


def scissors_win(p, u):
    if p == 'scissors' and u == 'paper':
        return True
    return False


def rock_win(p, u):
    if p == 'rock' and u == 'scissors':
        return True
    return False


def is_win(pc, user):
    if pc == user:
        print(f'There is a draw ({pc})')
        return 50
    if paṕer_win(user, pc) or scissors_win(user, pc) or rock_win(user, pc):
        print(f'Well done. Computer chose {pc} and failed')
        return 100

    print(f'Sorry, but computer chose {pc}')
    return 0


def check_rating(user):
    file = open('rating.txt')
    for line in file:
        if line.split(' ')[0] == user:
            return int(line.split(' ')[1])
    return 0


user_name = input('Enter your name: ')
print(f'Hello, {user_name}')
score = check_rating(user_name)

while True:
    n = random.randrange(1, 4)
    pc_choice = options[n]
    user_choice = input().lower()

    if user_choice == '!rating':
        print(f'Your rating: {score}')
        continue

    if user_choice not in options.values():
        print('Invalid input')
        continue

    if user_choice == '!exit':
        break

    score += is_win(pc_choice, user_choice)

print('Bye!')

