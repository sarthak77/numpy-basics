import numpy as np

a=np.arange(15).reshape(3,5)
print(a)

"""
The shape of an array can be changed with various commands. Note that
the following three commands all return a modified array, but do not
change the original array:
"""

print(a.ravel())#one row
print(a.reshape(1,15))
print(a.T)#transpose
print(a)

#to resize the original array

a.resize(5,3)
print(a)
print(a.reshape(1,-1))#-1 figures out the dimension