from turtle import *
showturtle()
shape("turtle")
color("HotPink")

fillcolor("Orange")
pensize(5)
# 변 개수 입력 받고 다각형 그리기

begin_fill()
n = int(input("변 개수 : "))
for i in range(n):
    fd(100)
    rt(360//n)

end_fill()
exitonclick()
