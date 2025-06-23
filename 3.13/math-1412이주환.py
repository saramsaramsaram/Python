import math
lst = list(range(1,11))

print(lst)

mean = sum(lst) / len(lst)
print("평균:", mean)


# 분산
vsum = 0
for i in lst:
    vsum += (i - mean) ** 2
variance = vsum / len(lst)
print("분산:", variance)

# 표준편차
stddev = math.sqrt(variance)
print("표준편차:", stddev)

# 최대 공약수 최소 공약수
gcd = math.gcd(10, 20)
lcm = math.lcm(10, 20)
print("최대공약수:", gcd)
print("최소공배수:", lcm)