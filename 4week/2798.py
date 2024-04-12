n,m = map(int,input().split())
cards = list(map(int, input().split()))
cards.sort()
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= m:
                result = max(result, sum)
print(result)