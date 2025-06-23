l = []
while True:
    i = float(input('입력: '))
    if i >= 0:
        l.append(i)
    else:
        break
print(sum(l) ,round(sum(l)/len(l), 1))