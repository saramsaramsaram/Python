import random as r
import time
cnt = 1
w = ["cat", "dog", "fish", "한나리", "유니티", "백엔드 ㅗㅗ", "응디", "파이썬"]
input("타자게임, Enter를 눌러 시작하세요.")
starttime = time.time()
while cnt <= 5:
    print(f'=== {cnt} 문제 ===')
    w_index = r.randint(0, len(w)-1)
    word = w[w_index]
    print(word)
    ans = input("타자: ")
    if ans == word:
        print("정답!")
        del w[w_index]
        cnt += 1
    else:
        print("허접♡")
endtime = time.time()
print((f'타자 시간: {endtime - starttime:.2f}초'))

