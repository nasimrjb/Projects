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


# def letterCounter(a, b):
#     return a.count(b)


# a = input("please input the word")
# b = input('input the letter')
# c = letterCounter(a, b)
# print(c)

# def multiple_letter_count(a):
#     b = {i: a.count(i) for i in a}
#     return b


# print(multiple_letter_count(input("input string: ")))

'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

# def list_manipulation(a,b,c):
#     if b == "remove":
#         if c == "end":
#             return a.pop()
#     if


# def is_palang(a):
#     b = [a[i] for i in range(len(a)-1, 0, -1)]
#     return print(b)


# is_palang(input())
# def frequency(a, b):
#     print(a.count(b))


# a = input("input a list: ")
# b = input("input the word")
# frequency(a, b)
# def multiply_even_numbers(lst):
#     total = 1
#     for val in lst:
#         if val % 2 == 0:
#             total = total * val
#     print(total)

# def intersection(a, b):
#     [i for i in a if i in b]

def isEven(num):
    return num % 2 == 0


def partition(a, b):
    lst1 = []
    lst2 = []
    for i in a:
        if b(i):
            lst1.append(i)
        else:
            lst2.append(i)
    print([lst1] + [lst2])


partition([1, 2, 3, 4], isEven)  # [[2,4],[1,3]]
