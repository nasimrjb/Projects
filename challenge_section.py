
# def two_list_dictionary(l1, l2):
#     dct = {}
#     for i, val in enumerate(l1):
#         dct[l1[i]] = l2[i]
#     else:
#         dct[l1[i]] = None
#     return dct
# def two_list_dictionary(keys, values):
#     collection = {}

#     for idx, val in enumerate(keys):
#         if idx < len(values):
#             collection[keys[idx]] = values[idx]
#         else:
#             collection[keys[idx]] = None

#     return collection


# l1 = ['x', 123, 45, "things", "keys"]
# l2 = ['rt', "hello", 34, '45']

# print(two_list_dictionary(l1, l2))

###########################################################
# def range_in_list(lst, start, end):
#     sum = 0
#     for i, j in enumerate(lst, start):
#         if i <= end:
#             sum += lst[i]
#     return sum


# print(range_in_list([0, 1, 2, 3, 4, 5, 6, 7, 8], 3, 7))
###########################################################
# def nth(lst, num):
#     for i in lst:
#         if lst[num] == i:
#             return i


# print(nth([1, 2, 3, 4, 5, 6, 7, 8], -2))
###########################################################
# def find_the_duplicate(arr):
#     for i in arr:
#         for j in arr:
#             if i != j:
#                 if arr[i] == arr[j]:
#                     return arr[i]
#     else:
#         return None


# print(find_the_duplicate([1, 2, 3, 4, 5, 1, 7, 9, 8]))


##########################################################
def sum_up_diagonals(lst):
    first = 0
    second = 0
    for i, j in enumerate(lst):
        first += lst[i][i]
        second += lst[i][-i-1]
    print(first)
    print(second)


print(sum_up_diagonals(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))


#############################################################
