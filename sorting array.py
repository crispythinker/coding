a = [1,34,2,54,33,23]
n = len(a)
temp = 0
for i in range(n-1):
    if a[i] > a[i+1]:
        temp = 0
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
print(a)