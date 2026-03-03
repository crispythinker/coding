a = [10,10,10,3,2,4,6,0,1,1,1,1]
b = []
for i in a:
    if i in b:
        continue
    else:
        b.append(i)

print(b)