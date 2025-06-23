row, col = map(int, input('행 수, 열 수: ').split())
for i in range(1, col*row+1):
    print(i, end=' '); print() if i % col == 0 else None