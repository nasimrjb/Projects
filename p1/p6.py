# ask for age
# 18 - 21 wristband
# 21+ drink, normal entry
# too young, sorry

age = input("how old are  you: ")

# if age != "":
# if age:
#     age = int(age)
#     if 18 <= age < 21:
#         print("you can enter, but need a wristband!")
#     elif age >= 21:
#         print('ok, you\'re good to go')
#     else:
#         print('you can\'t come in,little one!')
# else:
#     print('please enter an age!')

if age:
    age = int(age)
    if age >= 21:
        print("ok, you\'re good to go!")
    elif age >= 18:
        print('you can enter, but need a wristband!')
    else:
        print('you can\'t come in,little one!')
else:
    print('please enter an age!')
