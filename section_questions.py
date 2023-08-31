# def reverse_string(string):
#     return string[::-1]


# print(reverse_string("Nasimoo"))

####################################################


# def is_list(lst):
#     for l in lst:
#         if type(l) != list:
#             return False
#     return True


# print(is_list([[1], [1, 2], [], [2, 3, 4]]))


####################################################
def remove_every_oder (lst):
    l =[]
    for i in range (len(lst)-1):
        if i%2 == 0:
            