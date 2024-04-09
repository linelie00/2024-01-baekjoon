arr = input()
c = 0
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        c += 1 
print((c+1)//2)