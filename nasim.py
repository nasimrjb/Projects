import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


# my_list = [1, 2, 3, 4]             # Define a list

# my_array = np.array(my_list)       # Pass the list to np.array()

# print(my_array)
# print(my_list)

# print(np.identity(n=5))

# my_dict = {"x": 2, "a": 5, "b": 4, "c": 8}

# my_series2 = pd.Series(my_dict)
# print(my_series2)

# my_series = pd.Series(index=[2, 3, 5, 4],             # Data
#                       data=['a', 'b', 'c', 'd'])
# print(my_series)


###########################################################################################


# my_dict = {"name": ["Joe", "Bob", "Frans"],
#            "age": np.array([10, 15, 20]),
#            "weight": (75, 123, 239),
#            "height": pd.Series([4.5, 5, 6.1],
#                                index=["Joe", "Bob", "Frans"]),
#            "siblings": 1,
#            "gender": "M",
#            "IQ": 100}

# my_dict = {"name": ["Joe", "Bob", "Frans"],
#            "age": np.array([10, 15, 20]),
#            "weight": (75, 123, 239),
#            "height": [4.5, 5, 6.1],
#            "siblings": 1,
#            "gender": "M",
#            "IQ": 100}

# df = pd.DataFrame(my_dict)

# # print(df)

# df2 = pd.DataFrame(my_dict,
#                    index=my_dict["name"])

# print(df2)

# x = np.array([10, 15, 20])
# y = pd.Series([1, 2, 3], [4.5, 5, 6.1])

# print(x)
# print(y)

# print(df["weight"])
# print(df.weight)
# print(df.loc["Joe"])
# print(df.loc["Joe", "IQ"])
# print(df.loc["Joe":"Bob", "siblings":"IQ"])
# print(df2.iloc[0])  # Get row 0
# print(df2.iloc[0:2, 5:8])
# print(df2.index[0:1])

###########################################################################################


# def generate_and_plot_normal_samples(n, mean=0, std_dev=1):
#     # Generate N samples from a normal distribution
#     samples = np.random.normal(mean, std_dev, n)

#     # Plot the samples on a histogram
#     plt.hist(samples, bins=30, density=True)

#     # Plot the normal distribution curve
#     x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
#     y = np.exp(-((x - mean) / std_dev)**2 / 2) / (std_dev * np.sqrt(2 * np.pi))
#     plt.plot(x, y, 'r--')

#     plt.xlabel('Value')
#     plt.ylabel('Frequency')
#     plt.title('Histogram of Normal Distribution Samples')
#     plt.show()


# # Generate and plot 1000 samples from a standard normal distribution
# generate_and_plot_normal_samples(1000)


###########################################################################################


# input = [
#     {
#         'key': 'list1',
#         'values': [4, 5, 2, 3, 4, 5, 2, 3],
#     },
#     {
#         'key': 'list2',
#         'values': [1, 1, 34, 12, 40, 3, 9, 7],
#     }
# ]


# def std_dic(input):
#     return {input[0]['key']: np.std(input[0]["values"]), input[1]['key']: np.std(input[1]["values"])}


# print(std_dic(input))


############################################################################################

# data = {'Name': ['John', 'Cataline', 'Matt'],
#         'Age': [50, 45, 30],
#         'City': ['Austin', 'San Francisco', 'Boston'],
#         'Marks': [70, 80, 95]}

# # Create a DataFrame df
# df = pd.DataFrame(data)
# print(df)

# data = {'units': [1, 2, 3, 4, 5],
#         'price': [7, 12, 8, 13, 16]}
# # Create a DataFrame df
# df = pd.DataFrame(data)

# df.plot(x='units', y='price')

# combined = [a + b for a in "life" for b in "study"]
# print(combined)

# words = ["life", "is", "study"]
# word_lengths = [4, 2, 5]
