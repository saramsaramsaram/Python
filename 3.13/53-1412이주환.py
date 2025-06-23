
def f_create():
    return list(map(int, input('정수 입력하세요: ').split()))

def f_append():
    global l
    try:
        a = int(input('정수 입력하세요: '))
    except ValueError:
        return False
    else:
        l.append(int(a))
        return True
while True:
    if not f_append():
        break
l = f_create()
print(l)
print('리스트의 평균:', sum(l)/len(l))
print('리스트의 합:', sum(l))