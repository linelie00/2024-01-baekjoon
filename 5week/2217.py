N = int(input())
arr = []
for i in range(N):
    arr.append(int(input())*(N-i))
    # arr[i] = arr[i] * (N-i)
print(max(arr))