# Sliding Window Technique
# O(n*2)-->O(n)

#Concepts
# Fixed window (size = K)
# Variable window (size <= K)

arr = [2,5,1,8,2,9]
k = 3
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, len(arr)):
    window_sum += arr[i] #add next element
    window_sum -= arr[i-k] #remove first element of previous window 
    max_sum = max(max_sum, window_sum)
print(max_sum)