# two ponter technique
# ek pointer start se aur ek pointer end se
# left = 0
# right = len(arr) - 1
#use: reverse array, check palindrome, find pair with given sum, merge two sorted arrays

# Traversal Technique
arr = [3,4,5,6,7]
rev = []
for i in range(len(arr)-1,-1,-1):
#start =len(arr)-1 se start hoga aur -1 tak jayega aur step -1 hoga
    rev.append(arr[i])
print(rev)

# Two pointer technique
arr = [3,4,5,6,7]
start = 0
end = len(arr) - 1
while start < end:
    arr[start], arr[end] = arr[end],arr[start]
    start += 1
    end -= 1
print(arr)

#pallindrome check
arr = [1,2,3,2,1]
start = 0
end = len(arr)-1
is_pallindrome = True
while start < end:
    if arr[start] != arr[end]:
        is_pallindrome = False
        break
    start += 1
    end -= 1
print(is_pallindrome)

#zeros move krna
arr = [0,1,0,3,12]
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j] ,arr[i] = arr[i] ,arr[j]
        j += 1
print(arr)