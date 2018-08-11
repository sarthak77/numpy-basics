import numpy as np

a=np.arange(16).reshape(2,8)
b=np.arange(16,32,1).reshape(2,8)
print(a,b)

print(np.vstack((a,b)))#places together vertically
print(np.hstack((a,b)))#places together horizontally

#column_stack
"""
The function column_stack stacks 1D arrays as columns into a 2D array.
It is equivalent to hstack only for 2D arrays:
"""
print(np.column_stack((a,b)))
x=np.array([1,2])
y=np.array([3,4])
print(np.column_stack((x,y)))

from numpy import newaxis
print(x[:,newaxis])#convert to column

"""
On the other hand, the function row_stack is equivalent to vstack for
any input arrays. In general, for arrays of with more than two
dimensions, hstack stacks along their second axes, vstack stacks along
their first axes, and concatenate allows for an optional arguments
giving the number of the axis along which the concatenation should
happen.
"""

print(np.r_[1:9:1,55])
print(np.c_[1:9:1])