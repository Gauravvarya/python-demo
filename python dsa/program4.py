# array me ek element kitni bar aaya
arr = [3,5,6,7,3,3,3]
target = 3
count = 0
for num in arr:
    if num == target:
        count += 1
print(count)

# element present h ya ni
arr = [3,4,5,4,5,4]
found = False
for num in arr:
   if num == 9:
      found = True
print(found)

# 2nd largest element
arr = [3,4,6,6,7,7,8]
first = second = -9999
for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print(second)

#unique element
arr = [2,5,4,6,4,7]
unique = []
for num in arr:
    if num not in unique:
        unique.append(num)
print(unique)
