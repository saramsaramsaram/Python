import random as r
c = int(input('입력(1:가위, 2:바위, 3:보): '))
l = [1,2,3]
_l = r.choice(l)
d = {1:2,2:3,3:1}
print(f'user : {c}, computer : {_l}', end=' ')
if c == _l:
    print('draw')
elif d[c] == _l:
    print('lose')
else:
    print('win')




# elif _l == (c+1)%3:
#     print('lose')
# else:
#     print('win')
