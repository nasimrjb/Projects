num_1 = input("Please input miles ")
num_2 = float(num_1) * 1.60934
print('{} miles equals to {} kilometers' .format(num_1, num_2))

######################

num_3, num_4 = input('enter 2 numbers: ').split()
num_3 = int(num_3)
num_4 = int(num_4)

sum_1 = num_3 + num_4
difference = num_3 - num_4

print("{} + {} = {}".format(num_3, num_4, sum_1))
print("{} - {} = {}".format(num_3, num_4, difference))

######################

first = "Venus"
last = "Williams"
formatted = "First Name: {}, Last Name: {}".format(first, last)
first = "Venus"
last = "Williams"
formatted = f"First Name: {first}, Last Name: {last}"
