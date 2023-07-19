# Empty Array in NumPy
# Default DataType is Float

import numpy as np

# 1 Dimensional Array
a = np.empty(3)
print(a)
print(type(a))
print("Dimensions: ", a.ndim)
print("Data Type: ", a.dtype)

# 2 Dimensional Array
b = np.empty([2, 3], dtype=object)
print(b)
print(type(b))
print('Dimensions: ', b.ndim)

# 3 Dimensional Array
c = np.empty([3, 2, 4], dtype=int)
print(c)
print(type(c))
print('Dimensions: ', c.ndim)
