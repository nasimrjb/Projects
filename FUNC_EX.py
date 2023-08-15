# def product(a, b):
#     return a*b


# a =
# b = input("give me the 2nd number: ")

# print(product(int(a), int(b)))


'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''


# def return_day(x):
#     dictt = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
#              4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
#     if dictt.get(x):
#         return dictt.get(x)
#     else:
#         return None


# print(return_day(int(input())))


'''
last_element([1,2,3]) # 3
last_element([]) # None
'''


# def last_element(a):
#     if a[-1]:
#         return a[-1]
#     else:
#         return None


# print(last_element(list(input())))

'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''


# def number_compare(a, b):
#     if a > b:
#         print("first is greater")
#     elif a < b:
#         print("second is greater")
#     else:
#         print("numbers are equal")


# a = input('enter first number: ')
# b = input("enter 2nd number: ")

# number_compare(a, b)


def letterCounter(a, b):
    return a.count(b)


a = input("please input the word")
b = input('input the letter')
