ui = eval(input("Enter List:"))
l = []
count = 0
for i in ui:
    if i != 0:
        l.append(i)
    else:
        count  += 1
for i in range(count):
    l.append(0)

print(l)