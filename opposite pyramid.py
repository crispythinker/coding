n = int(input())

num = 2 * n

for i in range(n):
    print(" " * i, end="")
    
    for j in range(n - i):
        print(num, end=" ")
    
    print()
    num -= 2
