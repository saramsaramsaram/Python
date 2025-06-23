import random
while True:
    start = random.randint(1, 10)
    end = random.randint(start, 10)
    print(f'{start}부터 {end}까지의 합계: {(start + end) * (end - start + 1) // 2}')
    if start == end:
        break