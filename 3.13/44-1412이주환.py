row = int(input('행 수: '))
col = int(input('열 수: '))

# 행렬
for i in range(1,row+1):
    for j in range(1, col+1):
        print(j*i, end=' ')
    print()