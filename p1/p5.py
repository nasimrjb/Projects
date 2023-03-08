# name = input('enter your name here: ')
# if name == "Arya Stark":
#     print('Valar Morgulis')
# elif name == 'Jon Snow':
#     print('You know nothing :D')
# else:
#     print('carry on')


animal = input('enter your favourite animal: ')
number = input('input your favourite number: ')

# if animal == "" or number == "":    #doesnt check whether both are empty
# if bool(animal) ^ bool(number):

# ^ is bitwise xor. line 18 can be replaced with line 14

if (animal and not number) or (number and not animal):
    print("you should type both inputs")
elif animal and number:
    if str(animal) == 'khar' and int(number) == 2:
        print(animal + " and " + str(number) + " are my favourites too!")
    elif str(animal) == 'khar' and int(number) != 2:
        print(animal + " is my favourite but " + str(number) + " isn't!")
    elif str(animal) != 'khar' and int(number) == 2:
        print(animal + " isn't my favourite but " + str(number) + " is!")
    elif str(animal) != 'khar' and int(number) != 2:
        print('sorry, none of them are my favourites!')
else:
    print("you didn't say anything")
