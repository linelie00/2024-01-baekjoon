n,k = map(int,input().split())

s = [int(input()) for i in range(n)]

answer = [0 for i in range(k+1)]
answer[0] = 1
num = 1

for i in s:
    for j in range(i, k+1):
        answer[j] += answer[j-i]
        
print(answer[k])