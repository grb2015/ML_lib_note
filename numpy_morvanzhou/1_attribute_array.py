import numpy as np

python_list =[ [1,2,3],[4,5,6] ]  # #列表转化为矩阵
array = np.array(python_list)
print(array)

print('number of dim:',array.ndim)  # 维度
# number of dim: 2

print('shape :',array.shape)    # 行数和列数
# shape : (2, 3)

print('size:',array.size)   # 元素个数
# size: 6
