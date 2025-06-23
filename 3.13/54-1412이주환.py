def fun_s(n):
    if n<2:
        return 1
    else:
        return n*fun_s(n-1)
print(fun_s(1))
print(fun_s(10))
a = int(input('정수 입력하세요: '))
print(f'{a}의 팩토리얼: {fun_s(a)}')

