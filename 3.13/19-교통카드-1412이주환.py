fee = 850
card = int(input('카드: '))
# 방버ㅂ1
if card >= fee:
    print('가능')
else:
    print('불가능')
# 방법2
if card < fee:
    print('불가능')
else:
    print('가능')