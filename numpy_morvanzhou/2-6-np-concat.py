import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])

## 左右合并，其实就是把B矩阵放到A矩阵右边(后边）
D = np.hstack((A,B))       # horizontal stack
print(D)  # [1,1,1,2,2,2]
## 1 1  1 | 2 2 2
##        |
##
##
A1 = np.array([[1,2,3],[4,5,6]])
print(A1)

B1 = np.array([[7,8,9],[10,11,12]])
print(B1)
D1 = np.hstack((A1,B1))
print(D1)
#[[ 1  2  3 |  7  8  9]
# [ 4  5  6 | 10 11 12]]
