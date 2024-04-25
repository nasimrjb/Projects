# my_dict = {"nasim": 1, "rajabi": 2, "ghah": 3}
# print(my_dict.items())


# for i, j in enumerate("python"):
#     print(j)

# for i in zip(('a', 'b', 'c'), (1, 2, 3)):
#     print(i)

# sentence = """
# Have free hours and love children?
# """
# # output = [('have', 'free'),
# #           ('free', 'hours'),
# #           ('hours', 'and'),
# #           ('and', 'love'),
# #           ('love', 'children?')]
# sentence = sentence.strip()
# x = sentence.split(" ")

# j = [(x[i], x[i+1]) for i in range(len(x)-1)]
# print(j)


# input = "nasimrajabighahnavieh"
# output = "i"
# x = "nasim"


# def recurring(string):
#     characters = {}
#     for i, char in enumerate(string):
#         if char in characters:
#             return char
#         characters[char] = i
#     return None


# print(recurring(input))


import pandas as pd
import numpy as np
# my_list = [1, 2, 3, 4]             # Define a list

# my_array = np.array(my_list)       # Pass the list to np.array()

# print(my_array)
# print(my_list)

# print(np.identity(n=5))

# my_dict = {"x": 2, "a": 5, "b": 4, "c": 8}

# my_series2 = pd.Series(my_dict)
# print(my_series2)

my_series = pd.Series(index=[2, 3, 5, 4],             # Data
                      data=['a', 'b', 'c', 'd'])
# print(my_series)


my_dict = {"name": ["Joe", "Bob", "Frans"],
           "age": np.array([10, 15, 20]),
           "weight": (75, 123, 239),
           "height": pd.Series([4.5, 5, 6.1],
                               index=["Joe", "Bob", "Frans"]),
           "siblings": 1,
           "gender": "M",
           "IQ": 100}

df = pd.DataFrame(my_dict)

print(df)

# x = np.array([10, 15, 20])
# y = pd.Series([1, 2, 3], [4.5, 5, 6.1])

# print(x)
# print(y)

print(df["weight"])
print(df.weight)
print(df.loc["Joe"])
print(df.loc["Joe", "IQ"])
print(df.loc["Joe":"Bob", "siblings":"IQ"])
