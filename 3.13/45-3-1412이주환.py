a = int(input())
#반대로 별찍기
# for i in range(1,a+1):
#     print(' ' * (a-i) + '*' * i)
for i in range(1,a+1):
    for j in range(a-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()