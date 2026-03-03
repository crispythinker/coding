# # USING LIST
# def fnc(s):
#     s = list(s)
#     new = []
#     for i in s:
#         if i not in new:
#             new.append(i)
#         else:
#             new.remove(i)
#     if new == []:
#         return -1
#     return new[0]

# s = input("enter string:").lower()
# print(fnc(s))




# #USING DICTIONARY
# def fnc(s):
#     new = {}
#     for i in s:
#         if i not in new.keys():
#             new[i] = 1
#         else:
#             new[i] += 1
#     if new == []:
#         return -1
#     for ch in s:
#         if new[ch] == 1:
#             return ch

# s = input("enter string:").lower()
# print(fnc(s))
