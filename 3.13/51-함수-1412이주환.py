def fun_s(num):
    return sum([i for i in range(1, num+1)])
print(fun_s(10))
print(fun_s(100))
print(fun_s(1000))

#  -------------------------------------

def fun_fac(num):
    return_num = 1
    for i in range(1, num+1):
        return_num *= i
print(fun_fac(10))
print(fun_fac(100))
print(fun_fac(1000))