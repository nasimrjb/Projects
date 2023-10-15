
def two_list_dictionary(l1, l2):
    dct = {}
    for i in len(l1):
        dct[l1[i]] = l2[i]
    else:
        dct[l1[i]] = None


l1 = ['x', 123, 45, "things", "keys"]
l2 = ['rt', "hello", 34, '45']

print(two_list_dictionary(l1, l2))
