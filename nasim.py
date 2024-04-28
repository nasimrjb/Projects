def uncommon_words(a, b):
    a = a.split(" ")
    b = b.split(" ")
    c = [word for word in b if word not in a]
    c_inverse = [word for word in a if word not in b]
    print(c + c_inverse)


a = 'Geeks for Geeks god'
b = 'Learning from Geeks for Geeks'


uncommon_words(a, b)
