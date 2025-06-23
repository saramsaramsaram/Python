import random as r
u,c = sorted(list(map(int, input('2개입력(중복 ㄱㄴ): ').split()))), sorted(list(r.choices([i for i in range(1, 7)], k = 2)))
print(f'user : {u}, computer : {c}', end=' '); print('1등' if u == c else '2등' if u[0] in c or u[1] in c else '3등')
