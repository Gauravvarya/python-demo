def Sumofsquares(n):
    return sum(i**2 for i in range(1, n+1))
n = 0
n = int(input("Enter a number: "))
print("Sum of squares from 1 to", n, "is:", Sumofsquares(n) )