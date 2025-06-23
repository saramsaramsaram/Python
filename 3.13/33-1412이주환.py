while True:
    i = int(input('입력: '))
    if i == 0:
        break
    print('5의 배수가 아닙니다.' if i % 5 else '5의 배수입니다.')
print('종료')