def pal(s):
    
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            print(False)
            break
        else:
            left += 1
            right -= 1
        
    print(True)
s = input("Enter String:").lower()
pal(s)