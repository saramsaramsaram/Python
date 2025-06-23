s = {'학번':105, '번호':20, '이름': '홍길동'}
print(s['학번'])
print(s['번호'])
print(s['이름'])

print(s.get('이름'))

print(s.get('주소'))
print(s.keys())
print(list(s.keys()))
print(s.values())
print(list(s.values()))

print('이름' in s)
print('주소' in s)
