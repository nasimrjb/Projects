def separator(ls):
    a = [x for x in ls if x % 2 == 0]
    b = [y for y in ls if y % 2 == 1]
    return (a, b)
