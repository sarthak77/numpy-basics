import numpy as np

a=np.arange(12)
b=a
print(b is a)#no copy created

# Different array objects can share the same data. The view method
# creates a new array object that looks at the same data.

c=a.view()
print(c)
print(c is a)
c.shape=2,6
print(c)
print(a)
c[0,4]=99
print(a)#a changes