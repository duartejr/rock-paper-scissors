import random


def who_hits(x, options):
    len_op = len(options)
    half_len = (len_op - 1) // 2
    x_pos = options.index(x)
    last_p = x_pos + half_len

    if x_pos <= half_len:
        hits = options[x_pos+1: last_p+1]
    elif x_pos == len_op -1:
        hits = options[:half_len]
    else:
        hits = options[x_pos+1::]
        hits += options[0:half_len - len(hits)]

    return hits


def is_win(user, pc, elements):

    hits = who_hits(pc, elements)

    if pc == user:
        print(f'There is a draw ({pc})')
        return 50
    if user in hits:
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
elements = input().split(',')

if len(elements) == 1:
    elements = ['rock', 'paper', 'scissors']

print("Okay, let's start")

while True:
    n = random.randrange(0, len(elements))
    pc_choice = elements[n]
    user_choice = input().lower()

    if user_choice == '!rating':
        print(f'Your rating: {score}')
        continue

    if user_choice == '!exit':
        break

    if user_choice not in elements:
        print('Invalid input')
        continue

    score += is_win(user_choice, pc_choice, elements)

print('Bye!')

