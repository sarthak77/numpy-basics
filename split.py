import numpy as np

a=np.arange(24).reshape(2,12)
print(a)
print(np.hsplit(a,3))#split into 3 arrays
print(np.hsplit(a,(3,4)))#split after 3rd and 4th column

# vsplit splits along the vertical axis, and array_split allows one to
# specify along which axis to split.