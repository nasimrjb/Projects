
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
# def sum_up_diagonals(lst):
#     first = 0
#     second = 0
#     for i, j in enumerate(lst):
#         first += lst[i][i]
#         second += lst[i][-i-1]
#     print(first)
#     print(second)


# print(sum_up_diagonals(
#     [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))


#############################################################
# def min_max_key(dic):
#     result = {}
#     result[0] = max(dic.values())
#     result[1] = min(dic.values())
#     return result


# print(min_max_key({1: 3, 2: 5, 7: 11, 0: 12}))

###################################################################
# def find_greater_numbers(num):
#     count = 0
#     for i in num:
#         for j in num:
#             if i != j:
#                 if i < j:
#                     count += 1

#     print(count)


# find_greater_numbers([1, 2, 3])  # 3
# find_greater_numbers([6, 1, 2, 7])  # 4
# find_greater_numbers([5, 4, 3, 2, 1])  # 0
# find_greater_numbers([])  # 0
################################################################
# def two_oldest_ages(lst):
#     maxes = []
#     maxes.append(max(lst))
#     lst.remove(maxes[0])
#     maxes.append(max(lst))
#     return maxes


# print(two_oldest_ages([1, 50, 3, 6, 67, 34, 23, 45]))

###############################################################


# def is_odd_string(str):
#     count = 0
#     dct = {"a": 1, "b": 2, "c": 3, "d": 4, 'e': 5, "f": 6,
#            "g": 7, 'h': 8, 'i': 9, "j": 10, "k": 11, "l": 12}
#     for letter in str:
#         count += dct[letter.lower()]
#     if count % 2 == 0:
#         return False
#     return True


# print(is_odd_string("abccd"))
################################################################
# def three_odd_numbers(lst):
#     for i, j in enumerate(lst):
#         if (lst[i]+lst[i+1]+lst[i+2]) % 2 == 1:
#             return True
#         return False


# print(three_odd_numbers([2, 2, 4, 4, 4, 4, 4]))


###############################################################
# def mode(lst):
#     unique = set(lst)
#     dct = {}
#     for i in unique:
#         dct[i] = 0
#         for j in lst:
#             if j == i:
#                 dct[i] += 1
#     frequency = max(dct.values())
#     for r in dct:
#         if dct[r] == frequency:
#             print(r)


# mode([1, 2, 2, 2, 2, 2, 22, 3, 4, 4, 5, 4, 4, 4])

##############################################################
# def running_average():
#     running_average.accumulator = 0
#     running_average.size = 0

#     def inner(number):
#         running_average.accumulator += number
#         running_average.size += 1
#         return running_average.accumulator / running_average.size

#     return inner


# rAvg = running_average()
# print(rAvg(10))  # 10.0
# print(rAvg(11))  # 10.5
# print(rAvg(12))  # 11

# rAvg2 = running_average()
# print(rAvg2(1))  # 1
# print(rAvg2(3))  # 2


##############################################################
# def letter_counter(str):
#     def freq(l):
#         count = 0
#         for i in str:
#             if i == l:
#                 count += 1
#         return count
#     return freq


# counter = letter_counter('Amazing')
# print(counter('a'))  # 2
# print(counter('m'))  # 1

# counter2 = letter_counter('This Is Really Fun!')
# print(counter2('i'))  # 2
# print(counter2('t'))  # 1

#####################################################
