import numpy as np

a=np.arange(12)**2
print(a)
i=np.array([1,1,3,8,5])
print(a[i])#will print a[1],a[3],a[8]...
j=np.array([[3,4],[5,6]])
print(a[j])

a=np.arange(5)
a[[1,3,4]]=0
print(a)