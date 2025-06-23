print("^" * 20)
print("    연산프로그램")
print("^" * 20)

# a = int(input("첫번쨰 값 : "))
# b = int(input("두번쨰 값 : "))
a, b = map(int, input("값을 입력하세요. : ").split())

print("^" * 20 )

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} ** {b} = {a ** b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} % {b} = {a % b}') 