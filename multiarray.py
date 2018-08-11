import numpy as np

c=np.arange(12).reshape(2,2,3)
print(c)
print(c[1,:,:])
print(c[:,1,:])
print(c[:,:,2])


for i in c:
    print(c)

"""
However, if one wants to perform an operation on each element in the
array, one can use the flat attribute which is an iterator over all
the elements of the array:
"""

for i in c.flat:
    print(i)