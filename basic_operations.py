import numpy as np

a=np.arange(1,5,1)
b=np.arange(5,9,1)
print(a-b)
print(a**2)
print(a<2)
d=np.arange(1,5,1).reshape(4,1)
print(d)
print()
print(a@d)#matrix product or a.dot(b)
print(a*b)#elementwise product


x=np.arange(15).reshape(3,5)
print(x)
print(x.sum())
print(x.min())
print(x.max())
print(x.sum(axis=0))#sum of each column
print(x.sum(axis=1))#sum of each row
print(x.cumsum(axis=1))#cumulative sum along each row