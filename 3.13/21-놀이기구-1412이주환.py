h = int(input('키(cm): '))
w = int(input('몸무게(kg): '))
print('#'*20)
if 190 > h >= 130 and 100 > w >= 25:
    print('놀이기구에 탑승할 수 있습니다.')
else:
    print('놀이기구에 탑승할 수 없습니다.')