def reverse_string(string):
    return string[::-1]


print(reverse_string("Nasimoo"))

####################################################


def is_list(lst):
    for l in lst:
        if type(l) != list:
            return False
    return True


print(is_list([[1], [1, 2], [], [2, 3, 4]]))


####################################################
