cnt = 0
while cnt <= 5:
    i = int(input( '=========== \n돈을 넣어주세요: '))
    print('맛있는 주스 드세요.' if i == 800 else f'맛있는 주스 드시고 잔돈 {i - 800}원 받아가세요.' if i  > 800 else f'가격을 확인해 주세요. \n{i}')
    cnt += 1 if i >= 800 else 0
print('매진')













# if i == 800:
    #     print('맛있는 주스 드세요.')
    # elif i > 800:
    #     print(f'맛있는 주스 드시고 잔돈 {i - 800} 받아가세요.')
    # else:
    #     print(f'가격을 확인해 주세요. \n{i}')
    #     cnt -= 1