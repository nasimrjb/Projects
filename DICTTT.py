# inventory = {'croissant': 19, 'bagel': 4,
#              'muffin': 8, 'cake': 1}  # DON'T CHANGE THIS LINE!

# # Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD


# # add the value 18 to stock_list under the key "cookie"
# stock_list = inventory.copy()
# stock_list = dict(stock_list, cookie=18)
# stock_list.pop('cake')
# print(stock_list)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[i]: list2[i] for i in range(0, 3)}
# print(answer)

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# # use the person variable in your answer
# answer = {person[i][0]: person[i][1] for i in range(0, 3)}
# print(person[0][1])
# print(answer)

lst0 = {x: chr(x) for x in range(65, 91)}
print(lst0)
