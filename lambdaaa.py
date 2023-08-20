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
def max_magnitude(lst):
    result = []
    for i in lst:
        result.append(abs(i))
    print(max(result))


max_magnitude([1, 2, -900, 56, 10])
