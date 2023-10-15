
def two_list_dictionary(l1, l2):
    if len(l2)==len(l1):
        dict = {i: j for i in l1 for j in l2 if l1.index(i) == l2.index(j)}
    if len(l2) >len(l1):
        

l1 = ['x', 123, 45, "things"]
l2 = ['rt', "hello", 34, '45']

print(two_list_dictionary(l1, l2))
