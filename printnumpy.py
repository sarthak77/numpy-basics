import numpy as np
import sys

a=np.chararray((5,10))
a[:]="%"
a[1,3]="$"

sys.stdout.flush()
print(a)

for row in range(5):
    for column in range(10):
        b=a[row,column].decode()
        sys.stdout.write(b)
    sys.stdout.write("\n")