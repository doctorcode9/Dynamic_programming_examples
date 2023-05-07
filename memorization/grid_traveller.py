''' 
in this example we will see another application of the dynamic programminf technique
to solve a problem

we will use it to solve the grid traveller problem

'''

def gridTraveller(m,n, memo = {}):
    if (m == 1 and n == 1):
        return 1
    if (m == 0 or n == 0):
        return 0
    if ((m,n) in memo):
        return memo[(m,n)]
    memo[(m,n)] = gridTraveller(m-1,n) + gridTraveller(m, n-1)
    return gridTraveller(m-1,n) + gridTraveller(m, n-1)


print(gridTraveller(1,1))
print(gridTraveller(2,3))
print(gridTraveller(3,2))
print(gridTraveller(3,3))
print(gridTraveller(18,18))