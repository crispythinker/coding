arr = eval(input("Enter List Please:"))
k = int(input("Enter number of positions to shift:"))
def ra(arr,k):
    l = []
    r = []
    n = len(arr)
    k = k%n
    split = n - k
    for i in range(0,split):
        l.append(arr[i])
    for j in range(split,n):
        r.append(arr[j])
    res = r+l

    return res
    

print(ra(arr,k))