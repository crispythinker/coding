# s = input("Enter the string:")
# s = s.split(" ")
# def reverse_words_in_a_string(s):
#     l = 0
#     r = len(s) - 1
#     while l < r:
#         temp = s[l]
#         s[l] = s[r]
#         s[r] = temp
#         l += 1
#         r -= 1
#     return " ".join(s)
# print(reverse_words_in_a_string(s))


# EASY:
s = input("Enter the string:")
s = s.split(" ")
def reverse_words_in_a_string(s):
    s.reverse()
    return " ".join(s)
print(reverse_words_in_a_string(s))
