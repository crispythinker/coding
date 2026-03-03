l = [-4, -1,-2,-2]
sum = l[0]
curr = 0

start = 0
best_start = 0
best_end = 0


for i in range(len(l)):
    curr += l[i]
    if curr > sum:
        sum = curr
        best_start = start
        best_end = i

    print("Curr:",curr,"Sum:",sum)
    if curr < 0:
        curr = 0
        start = i+1



    print("Curr:",curr,"Sum:",sum,"Start:",start,"Best Start:",best_start,"Best End:",best_end)
    

print(l[best_start:best_end+1])
