import numpy as np

A = np.arange(3, 15).reshape((3, 4))

print(A.flatten())
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

for item in A.flat:
    print(item)
