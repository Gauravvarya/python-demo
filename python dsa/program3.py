#max element in array
arr = [3,7,2,9,3]
max_num = arr[0]#phle ye mana ki sbse bada element 1st element h
for num in arr:
    if num > max_num:
        max_num = num
print(max_num)

# min element in array
arr = [3,4,5,7,9]
min_num = arr[0]
for num in arr:
    if num < min_num:
     min_num = num
print(min_num)

#sum of array
arr = [3,5,8,6,7]
total = 0
for num in arr:
   total = total + num
print(total)

#reverse array
arr=[3,4,5,6,7,8]
rev =[]
for i in range(len(arr)-1,-1,-1):
   rev.append(arr[i])
   print(rev)

arr = [3,4,5,6,4]
rev = arr[::-1]
print(rev)