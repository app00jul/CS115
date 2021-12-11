def dotProduct(L, K):
    if L == [] and K == []:
        result = 0.0
    else:
        """
        How this works:
        list 1 is [1,2,3] and list 2 is [10,11,12]
        the first round: 1*10 + dotProduct()
        now the L[1:] is [2,3] and K[1:] is [11,12] are the new list
        the second round: L[0] will be understand as [2,3] instead of as [1,2,3] 
        same apply to K[0]
        """
        result = L[0] * K[0] + dotProduct(L[1:],K[1:]) 
    return result

lst_1 = [1,2,3]
lst_2 = [10,11,12]
print(dotProduct(lst_1,lst_2))

def removeAll(e,L):
    if e == L[0]:
        return L[1:] 
    else:
        return [L[0]] + removeAll(e,L[1:])


lst = [1,4,6,12,51,6]
print(removeAll(6,lst))


def deepReverse(L):
    return [L[-1]] + deepReverse(L[:-1])

print(deepReverse([1,3,4,5]))
