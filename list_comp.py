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

def find_factors(num):
  # return [x + 1 for x in range(num) if num % (x + 1) == 0 and x != 0]
    lst = []
    for i in range(num):
        if i != 0 and num % i == 0:
            lst.append(i)
    return lst


print(find_factors(400))
