from turtle import *

def input_data():
    x,y = map(int, input("n각형, 한변의 길이: ").split())
    return x,y

def moving():
    x,y = map(int, input("이동할 좌표를 입력하세요: ").split())
    up()
    goto(x,y)
    down()
    
def polygon(n):
    n,a = input_data()
    for i in range(n):
        forward(a)
        left(360/n)

moving()
input_data()