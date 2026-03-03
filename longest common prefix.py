arr = ["light",'lift','litt']

def longest_common_prefix(arr):
    prefix = ""
    for iterator in range(len(arr[0])):
        character  = arr[0][iterator]
        for word in arr:
            if iterator >= len(word) or word[iterator] != character:
                return prefix
        prefix += str(word[iterator])
    return prefix
print(longest_common_prefix(arr))