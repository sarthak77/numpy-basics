import numpy as np

a=np.array([2,3,4])
print(a)

b=np.arange(1,11,1).reshape(5,2)
print(b)

c=np.array([(1.5,2,3), (4,5,6),(1,2,3)])#2d array
print(c)

d=np.array([[(1.5,2,3), (4,5,6)],[(1,2,3),(5,6,7)]])#3d array
print(d)

e = np.array( [ [1,2], [3,4] ], dtype=complex )
print(e)

#####################################################################
"""
Often, the elements of an array are originally unknown, but its size
is known. Hence, NumPy offers several functions to create arrays with
initial placeholder content. These minimize the necessity of growing
arrays, an expensive operation.

The function zeros creates an array full of zeros, the function ones
creates an array full of ones, and the function empty creates an array
whose initial content is random and depends on the state of the memory.
By default, the dtype of the created array is float64.
"""
a=np.zeros((10,10))
print(a)

a=np.ones((10,10))
print(a)

a=np.empty((11,11))
print(a)

a=np.linspace(1,10,10)#from 1 to 10, 10 numbers
print(a)

a=np.random.random(10).reshape(5,2)
print(a)

def f(x,y):
    return (10*x+y)

a=np.fromfunction(f,(5,4))
print(a)