import random as rd
import sys

num_range = input(f'Hello! What range should I choose for my number? Example: “1 100”:\n')
num_range = num_range.split()
num = rd.randint(int(num_range[0]), int(num_range[1]))

def answer_check_more_less(num):
    answer = int(input(f'Try to guess the number:\n'))
    num = int(num)

    if answer > num:
        print(f'Less!')
    elif answer < num:
        print(f'More!')
    elif answer == num:
        print(f'Victory!')
        sys.exit()
    else:
        print(f'Invalid input!')

def answer_check_warm_cold(num):
    answer = int(input(f'Try to guess the number:\n'))
    num = int(num)

    if abs(answer - num) >= 100 and answer != num:
        print(f'Super cold!')
    elif abs(answer - num) >= 50  and answer != num:
        print(f'Cold!')
    elif abs(answer - num) >= 35 and answer != num:
        print(f'Warm!')
    elif abs(answer - num) >= 25 and answer != num:
        print(f'Warmer!')
    elif abs(answer - num) >= 10 and answer != num:
        print(f'Super warm!')
    elif abs(answer - num) >= 5 and answer != num:
        print(f'The hell!')
    elif answer == num:
        print(f'Victory!')
        sys.exit()
    else:
        print(f'Invalid input!')

tmp = input(f'Choose your option:'
            f'\n - 1. More/Less'
            f'\n - 2. Warm/Cold\n')
if tmp == '1':
    while True:
        answer_check_more_less(num)
elif tmp == '2':
    print(''
          '\n - 1. Super cold: diff > 100'
          '\n - 2. Cold: diff > 50'
          '\n - 4. Warm: diff > 35'
          '\n - 5. Warmer: diff > 25'
          '\n - 6. Super warm: diff > 10'
          '\n - 7. The hell!: diff > 5')
    while True:
        answer_check_warm_cold(num)
else: print('Invalid input!')
