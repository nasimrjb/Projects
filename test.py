import numpy as np
import pandas as pd
import scipy as scipy

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = np.array(x)
# print(x[3::1, -1])

tarr = np.random.randint(0, 10, (4, 3))
# print(tarr)


numbers = [2, 2.1, 3]
p_numbers = pd.Series(numbers)
# print(p_numbers)

animals = {
    'n1': 'Tiger',
    'n2': 'Bear',
    'n3': None
}
p_animals = pd.Series(animals)
# print(p_animals)

# print(p_animals.iloc[2])
