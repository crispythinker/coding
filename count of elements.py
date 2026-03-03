arr = [1, 1, 2, 3, 2]
d = {}
for i in arr:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1 

print(d)
        
