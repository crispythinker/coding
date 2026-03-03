a = [10,1,3,2,1,11]
l = r = 0
max = 0
for l in range(len(a) - 3):
    r = l + 2
    s = (a[l]+a[l+1]+a[r])
    if max < s:
        max = s
    
print(max)
