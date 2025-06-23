while True:
    try:
        n = int(input())
    except ValueError:
        print('숫자만 입력하세요')
    else:
        print(n)
        break
