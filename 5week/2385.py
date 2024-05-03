import math
N = int(input())
arr = []
min = 0
for i in range(N):
    arr.append(int(input()))
    if i == 1:
        min = arr[i] - arr[i-1]
    elif i > 1:
        min = math.gcd(min,arr[i]-arr[i-1])
        
print((arr[N-1]-arr[0])//min-N+1)

# 18 - 2 = 16
# n = 4, min = 4 6 [2]
# 12 n= 4 min=2