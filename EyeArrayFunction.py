# Eye Array Function in NumPy
# By Default Datatype is Float and K=0 index
# if you don't tell no of columns then it'll automatically be equal to no of rows.
import numpy as np


a = np.eye(3)
print(a)

# 2nd Diagonal with 1
b = np.eye(3, k=1)
print(b)
print("\n")

# Matrix with 2 rows and 3 columns:
c = np.eye(2, 3, dtype=int)
print(c)
print("\n")

# Matrix with 5 rows and 3 columns:
d = np.eye(5, 3, dtype=int)
print(d)
print("\n")

# Additional Example
j = np.eye(1)
print(j)

k = np.eye(2, dtype=str)
print(k)
