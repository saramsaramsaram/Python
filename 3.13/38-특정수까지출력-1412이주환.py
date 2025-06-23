a = int(input('어디까지: '))
for i in range(1, a + 1):
    print(i)


for i in range(a,9):
    print(i)

a = int(input('몇 단?:  '))
print(f' ==== {a}단 ====')
for i in range(1,10):
    print(f'{a} * {i} = {a * i}')