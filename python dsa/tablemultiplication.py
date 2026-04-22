# def printTable(n):
#     for i in range(1,11):
#         print("%d * %d = %d" % (n,i,n*i))

#         n = int(input("Enter a number: "))
#         printTable(n)

# def printTable(n):
#     for i in range(1, 11):
#         print("%d * %d = %d" % (n, i, n * i))


# n = int(input("Enter a number: "))
# printTable(n)

# recursive approach
def printTable(n, i =1):
    if i > 10:
        return
    print(n, "*", i, "=", n*i)
    i = i + 1
    printTable(n , i)
n = int(input("Enter a number: "))
printTable(n)