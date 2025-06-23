f = open("data_2.txt", "a")
for i in range(11,21):
    f.write(f'{i}번째 줄입니다.\n')
f.close()