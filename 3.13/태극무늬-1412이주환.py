from turtle import *

bgcolor("black")
pensize(1)

# 태극 무늬 그리기

#빨,노, 파를 번갈아 가며 적용
#한번 이동하는 거리를 2배씩 늘리기
# 119도씩 회전
#200번 반복

for i in range(200):
    if i % 3 == 0:
        color("red")
    elif i % 3 == 1:
        color("yellow")
    else:
        color("blue")

    fd(2**i)
    rt(119)
done()