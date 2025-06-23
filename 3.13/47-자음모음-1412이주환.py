# w = input("영문자열 입력: ")
# mo = ["a", "e", "i", "o", "u"]
a = 0
b = 0
digit = 0
special = 0
# for i in w:
#     if i.isalpha() == True:
#         if i in mo:
#             a += 1
#         else:
#             b += 1
# print("모음 개수:", a)
# print("자음 개수:", b)   

sen = input("문자열 입력: ")
mo = ["a", "e", "i", "o", "u"]
for i in sen:
    if i.isalpha():
        if i in mo:
            a += 1
        else:
            b += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        None
    else:
        special += 1