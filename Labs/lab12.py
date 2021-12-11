"""
Name: Julian Noeske
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
"""

import random
def shuffedNumbers(n):
    if n<0:
        return []
    else:
        out=list(range(0,n))
        i = 0
        for i in range(0,n):
            j = random.randint(0,i)
            if j < i:
                swap = out[i]
                out[i] = out[j]
                out[j] = swap
            i = i + 1
    return(out)

print(shuffedNumbers(10000000))

