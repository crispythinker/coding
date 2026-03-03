def twosum():
    a = [10,2,10,3,45]
    val = []
    target = 5
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] + a[j] == target:
                val.append((a[i],a[j]))
    return val

print(twosum())