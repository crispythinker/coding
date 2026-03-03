def rde(l):
    s = set()
    for i in l:
        if i not in s:
            s.add(i)
    return len(list(s))

l = eval(input("Enter list:"))
print(rde(l))
