a = int(input('자연수: '))
for i in range(1, a+1):
    if a % i == 0:
        print(i, end=' ')
print()

for i in range(a, 0, -1):
    if a % i == 0:
        print(i, end=' ')