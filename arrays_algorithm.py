array = ['a', 'b', 'c', 'd', 'e']


def returnpairs(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i], array[j])


returnpairs(array)
