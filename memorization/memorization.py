#using recursion only to make fibonnuci function
# 1 : this is a simple finbbouci algorithm
def Fibonnuci(n):
    if n <= 2 :
        return 1
    return (Fibonnuci(n-1) + Fibonnuci(n-2))

''' n = int(input("type a number to get the fibonncui sequence of the index: "))
print(Fibonnuci(n)) '''


# now let's use memorisation to optmize our algorith
memo = {}
def MemoFib(n):
    if n <= 2:
        return 1
    if n not in memo:
        memo[n] = MemoFib(n-1) + MemoFib(n-2)
    return memo[n]
    
    
    
    

n = int(input("type a number to get the fibonncui sequence of the index: "))
print(MemoFib(n))