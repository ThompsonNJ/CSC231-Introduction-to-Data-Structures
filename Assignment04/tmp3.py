import Stackarray as SA
import Stacklinked as SL
from time import time as gT


for y in 10000, 100000, 1000000, 10000000:
    print(y)
    t1 = gT()
    sa = SA.Stack()

    for x in range(y):
        sa.push(x)

    while not sa.is_empty():
        sa.pop()

    print("Array:",gT()-t1)

    t1 = gT()
    sl = SL.Stack()

    for x in range(y):
        sl.push(x)

    while not sl.is_empty():
        sl.pop()

    print("LList:",gT()-t1,'\n')

#END
