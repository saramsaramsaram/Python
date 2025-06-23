a = int(input('어디까지: '))
print(f'1부터 {a}까지의 합계d: {(1 + a)* a // 2}')

c = 1
for i in range(1, a + 1):
    c *= i
print(f'1부터 {a}까지의 곱: {c}')