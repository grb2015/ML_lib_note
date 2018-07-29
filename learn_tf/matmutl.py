# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-07-29 09:12:50
# @Last Modified by:   Teiei
# @Last Modified time: 2018-07-29 09:37:20
import tensorflow as tf
import numpy as np
#-----tf中的matmul 与* 类似numpy中的dot 和 *
print('------ 1. "matmul" 矩阵乘法--------------')
a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])
c = tf.matmul(a, b)


init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

print(c)
print("c =",sess.run(c) )

print('------ 2. "*" 普通乘法--------------')

x = tf.constant(np.array([[1,2],[3,4]]) )
y = tf.constant(np.array([[5,6],[7,8]]) )
print('x=\n',x)
print('y=\n',y)
print("x =",sess.run(x) )
print("y =",sess.run(y) )
z = x*y 
print('z=',z)
print("z =",sess.run(z) )