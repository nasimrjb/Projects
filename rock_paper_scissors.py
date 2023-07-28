from random import randint


a = input ("player 1's choice: ")
# print ("no cheating \n"*20)
# b = input ("player 2's choice: ")

c = randint(1,3)

if c == 1:
    b = "ROCK"
    print("Computer plays: " + b)
elif c == 2:
    b = "PAPER"
    print("Computer plays: " + b)
else:
    b = "SCISSORS"
    print("Computer plays: " + b)

if a.upper() == "ROCK":
    if b.upper() == "SCISSORS":
        print ("A WINS!")
    elif b.upper() == "PAPER":
        print("B WINS!")
    elif b.upper() == "ROCK":
        print("EQUAL!")
elif a.upper() == "PAPER":
    if b.upper() == "SCISSORS":
        print ("B WINS!")
    elif b.upper() == "PAPER":
        print("EQUAL!")
    elif b.upper() == "ROCK":
        print("A WINS")
elif a.upper() == "SCISSORS":
    if b.upper() == "SCISSORS":
        print ("EQUAL!")
    elif b.upper() == "PAPER":
        print("A WINS!")
    elif b.upper() == "ROCK":
        print("B WINS!")