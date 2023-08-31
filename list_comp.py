lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print([n for n in lst])

# print([n**2 for n in lst])
# print(list(map(lambda n: n * n, lst)))

# print([n for n in lst if n % 2 == 0])
# print(list(filter(lambda n: n % 2 == 0, lst)))

# lttr = 'abcd'

# print([(a, b) for a in lst for b in lttr])

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

print(dict(zip(names, heros)))
