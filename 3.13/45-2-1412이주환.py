a = int(input())
# for i in range(a,0,-1):
#     print('* ' * i)

for i in range(a,0,-1):
    for j in range(i):
        print('*',end='')
    print()