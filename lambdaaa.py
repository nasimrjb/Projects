# def cubes(x): return x*x*x


# print(cubes(3))

# lst = [1, 2, 3, 4, 5]

# dec_list = list(map(lambda x: x-1, lst))
# print(dec_list)


# def remove_negatives(lst):
#     print(list(filter(lambda x: x >= 0, lst)))


# remove_negatives([1, -3, 4, 5, -9, 0, -7])
# def extremes(l):
#     m = sorted(l)
#     return (m[0], m[-1])
# def max_magnitude(lst):
#     result = []
#     for i in lst:
#         result.append(abs(i))
#     print(max(result))


# max_magnitude([1, 2, -900, 56, 10])


# def sum_even_numbers(*args):
#     print(sum(arg for arg in args if arg % 2 == 0))

# sum_even_numbers(1, 2, 3, 4, 5, 6)
# def sum_floats(*args):
#     print(sum(arg for args in args if type(arg) == float))
# def interleave(str1, str2):
#     a = ["".join(x) for x in tuple(zip(str1, str2))]
#     print("".join(a))


# str1 = "salam "
# str2 = "olaghe"

# # interleave(str1, str2)
# def triple(lst):
#     print(list(map(lambda x: x*3, filter(lambda x: (x % 4) == 0, lst))))


# triple([1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 24])


# def extract(lst):
#     print([" ".join(lst[0].values()), " ".join(lst[1].values())])


# names = [{'first': 'Elie', 'last': 'Schoppik'},
#          {'first': 'Colt', 'last': 'Steele'}]
# extract(names)  # ['Elie Schoppik', 'Colt Steele']


# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct type of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

# Examples


def divide(num1, num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Please provide two integers or floats")
    except ZeroDivisionError:
        print("Please do not divide by zero")


divide(4, 2)
divide([], "1")  # "Please provide two integers or floats"
divide(1, 0)  # "Please do not divide by zero"
