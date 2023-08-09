from random import randint

a = randint(1, 10)
guess = 12345

while True:
    guess = input("input your guess between 1 and 10: ")
    if int(guess) > a:
        print("your guess is too high!")
    elif int(guess) < a:
        print("your guess is too low!")
    else:
        print("you won!")
        retry = input('do you wanna try again?:(y/n) ')
        if retry == 'n':
            break
        else:
            a = randint(1, 10)
            guess = 12345
