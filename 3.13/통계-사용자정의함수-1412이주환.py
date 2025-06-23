import math

def f_avg(l):
    return sum(l) / len(l)
def f_var(l):
    return sum((x - f_avg(l)) ** 2 for x in l) / len(l)
def f_std(l):
    return math.sqrt(f_var(l))
def f_comm(l):
    return math.gcd(*l), math.lcm(*l)
def f_input():
    return list(map(int, input("정수 리스트를 입력하세요: ").split()))
_l = f_input()
print("평균:", f_avg(_l))
print("분산:", f_var(_l))
print("표준편차:", f_std(_l))
print("최대공약수, 최소공배수:", f_comm(_l))
