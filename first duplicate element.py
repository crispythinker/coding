def fde(l):
    d = {}
    for num in range(len(l)):
        if l[num] not in d:
            d[l[num]] = 1
        else:
            d[l[num]] += 1
        for i in d:
            if d[i] > 1:
                return i

    print(d)
    return -1

l = eval(input("Enter list:"))
print(fde(l))