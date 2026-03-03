s1 = input("Enter S1:").lower()
s2 = input("Enter S2:").lower()
def anagram(s1,s2):
    d1 = {}
    d2 = {}
    if len(s1) != len(s2):
        return False
    for i in s1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for i in s2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1

    print(d1,d2)
    if d1 == d2:
        return True
    else:
        return False

print(anagram(s1,s2))