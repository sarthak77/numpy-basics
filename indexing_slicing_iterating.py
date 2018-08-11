import numpy as np

a=np.arange(10)
print(a)
print(a[2])
print(a[2:7:2])#i=2,i<7,i++
a[:6:2]=110
print(a)
print(a[ : :-1])#reverse array

for i in a:
    print(i**2)


def f(x,y):
    return (10*x+y)

b=np.fromfunction(f,(5,4))
print(b)
#       row  column ##i=0,i<n;i++
print(b[1:4:1,2])
print(b[-1,:])
print(b[-1,::])