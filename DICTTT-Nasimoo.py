# user_info = {"name": "Nasim", "age": 32, "sex": "F"}
# print(user_info)

# artist = {
#     "first": "Neil",
#     "last": "Young",
# }
# full_name = artist["first"] + " " + artist["last"]
# print(full_name)


# # DON'T TOUCH PLEASE!
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
#                  stan=150.0, lisa=50.25, harrison=10.0)
# # DON'T TOUCH PLEASE!


# # Use a loop to add together all the donations and store the resulting number in a variable called total_donations

# This code picks a random food item:
from random import choice  # DON'T CHANGE!
food = choice(["cheese pizza", "quiche", "morning bun",
              "gummy bear", "tea cake"])  # DON'T CHANGE!

# DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("nadarim")
