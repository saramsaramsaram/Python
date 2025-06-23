fr = []
while len(fl) < 5:
    fi = (input('입력: '))
    print('중복') if fi in fr else fr.append(fi)
print(fr)   