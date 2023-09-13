lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print([n for n in lst])

# print([n**2 for n in lst])
# print(list(map(lambda n: n * n, lst)))

# print([n for n in lst if n % 2 == 0])
# print(list(filter(lambda n: n % 2 == 0, lst)))

# lttr = 'abcd'

# print([(a, b) for a in lst for b in lttr])

#########################################################

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# print(dict(zip(names, heros)))

##########################################################
# def sum_pairs(lst, num):
#     for i in lst:
#         for j in lst:
#             if i != j:
#                 if i + j == num:
#                     return (i, j)


# print(sum_pairs(lst, 5))

##########################################################

# def vowel_count(str):
#     return {a: str.lower().count(a) for a in str if a in "aeiou"}


# print(vowel_count("absdanASDLDFkeepiooojsdaldsdskaasald"))

#########################################################

# def titleize(string):
#     lst = []
#     strr = ""
#     for i in string.split():
#         lst.append(i[0].upper() + i[1:] + " ")
# 1
#     m = ''.join(lst)
#     return m
# 2
# for j in lst:
#     strr += j
# return strr


# def titleize(string):
# return ' '.join(s[0].upper() + s[1:] for s in string.split())


# print(titleize("My name is Nasim"))
#############################################################

# string = "my name is nasim rajabi"

# print(' '.join(string.split()))

###############################################

# def find_factors(num):
#   # return [x + 1 for x in range(num) if num % (x + 1) == 0 and x != 0]
#     lst = []
#     for i in range(num):
#         if i != 0 and num % i == 0:
#             lst.append(i)
#     return lst


# print(find_factors(400))


####################################################

# def includes(collection, val, start=None):
#     if type(collection) == dict:
#         return val in collection.values()
#     if start == None:
#         return val in collection
#     else:
#         return val in collection[start:]


# print(includes([1, 2, 3], 1))  # True
# print(includes([1, 2, 3], 1, 2))  # False
# print(includes({'a': 1, 'b': 2}, 1))  # True
# print(includes({'a': 1, 'b': 2}, 'a'))  # False
# print(includes('abcd', 'b'))  # True
# print(includes('abcd', 'e'))  # False

#######################################################


# def repeat(string, num):
#     str1 = ""
#     for i in range(num):
#         str1 += string
#     print(str1)


# repeat('*', 3)  # '***'
# repeat('Nasim Rajabi', 2)  # 'abcabc'
# repeat('abc', 0)  # ''


#######################################################

# def truncate(str, num):
#     if num < 3:
#         print("Truncation must be at least 3 characters.")
#     elif num >= len(str) + 3:
#         return (str)
#     new_str = ''
#     for i in range(num - 3):
#         new_str += str[i]
#     print(new_str + "...")


# truncate("Super cool", 2)  # "Truncation must be at least 3 characters."
# truncate("Super cool", 1)  # "Truncation must be at least 3 characters."
# truncate("Super cool", 0)  # "Truncation must be at least 3 characters."
# truncate("Hello World", 6)  # "Hel..."
# truncate("Problem solving is the best!", 10)  # "Problem..."
# truncate("Another test", 12)  # "Another t..."
# truncate("Woah", 4)  # "W..."
# truncate("Woah", 3)  # "..."
# truncate("Yo", 100)  # "Yo"
# truncate("Holy guacamole!", 152)  # "Holy guacamole!"


####################################################################
