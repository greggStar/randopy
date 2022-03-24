import os
import keyboard
import random
import cmd, sys

def display_intro_bar():
    os.system('clear')

    print('\t=========================================================')
    print('\t*************************LOTTO***************************')
    print('\t=========================================================')


def get_user_choice():
    print('\n[1] Lucky dip')
    print('[2] Own numbers')
    print('[q] gambling is bad, walk out of shop')

    return input('What do you want mate? ')

def lucky_dip():
    return random.randint(1,49)

def get_user_numbers():
    return input('what numbers do you want?')

def display_numbers(data):
    os.system('clear')

    print('Your numbers are ')
    print(data)
    input('Press to continue')


if __name__ == '__main__':
    display_intro_bar()

    number = None
    choice = ''

    choice = get_user_choice()

    while choice != 'q':
        if choice == '1':
            number = lucky_dip()
        elif choice == '2':
            number = get_user_numbers()

        display_numbers(number)
