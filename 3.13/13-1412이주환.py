a = list(map(int, input('a: ').split()))
b = list(map(int, input('b: ').split()))
print('#' * 20)
print(f'합집합: {list(set(a) | set(b))}')
print(f'교집합: {list(set(a) & set(b))}')
print(f'차집합: {list(set(a) - set(b))}')