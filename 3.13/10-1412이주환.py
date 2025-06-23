data = [30,10,20]
print(f'현재 리스트: {data}')
print(f'리스트 데이터 개수: {len(data)}')
data.append(40)
print(f'40 추가 후의 리스트: {data}')
last = data.pop(len(data)-1)
print(f'리스트 마지막: {last}')
print(f'추출 후 리스트: {data}')
data.sort()
print(f'정렬: {data}')
data.reverse()
print(f'역순: {data}')
print(f'20의 위치: {data.index(20)}')
data.insert(2,222)
print(f'222 2에 삽입하고 리스트: {data}')
data.remove(222)
print(f'222 삭제 후: {data}')
data2 = [77,88,77]
data += data2
print(f'리스트 연결: {data}')
print(f'77의 개수: {data.count(77)}')
del data[2]
print(f'삭제: {data}')