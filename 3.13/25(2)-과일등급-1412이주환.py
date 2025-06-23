w = int(input('과일 무게(g): '))
if 375<=w or w<210:
    print('"판정 불가"')
elif w>=300:
    print('"특"')
elif w>=250:
    print('"상"')
else:
    print('"보통"')
# print('판정불가' if w>=375 or w<210 else '특' if w>=300 else '상' if w>=250 else '보통')