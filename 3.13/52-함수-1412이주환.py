def maxp(a,b):
    return max(a,b)

print(f'큰 수: {maxp(10,20)}')
a, b = map(int, input('두 수를 입력하세요: ').split())
print(f'큰 수: {maxp(a,b)}')