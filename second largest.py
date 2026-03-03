arr = [10,100,1,13333,443,32,1,1000,232111111]
f = 0
s = 0
for i in range(len(arr)):
    if arr[i] > f:
        s = f
        f = arr[i]
    elif arr[i] < f and arr[i] > s:
        s = arr[i]

print(f,s)
