def pal(a):
    l = 0
    r = len(a)-1
    while l < r:
        print(a[l],a[r])
        if a[l] == a[r]:
            l += 1
            r -= 1
            continue

        elif not 'a'<= a[l] <= 'z' and not '0'<= a[l] <= '9':
            l += 1
            print("After Left Increment:",a[l],a[r])
        elif not 'a'<= a[r] <= 'z' and not '0'<= a[r] <= '9':
            r -= 1
            print("After Right Increment:",a[l],a[r])
        else:
            return False
    return True

s = input("Enter a string:").lower()
print(pal(s))
    

