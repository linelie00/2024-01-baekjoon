import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = []
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    arr.sort()
    count = 1
    min = arr[0][1]
    for i in range(1,N):
        if arr[i][1] < min:
            count += 1
            min = arr[i][1]
    print(count)