l = eval(input("Enter list:"))
def me(l):
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1 

    for i,j in d.items():
        if j > len(l)//2:
            return i
print(me(l))