f = open("data_3.txt", "w")
while True:
    content = input("내용을 입력하세요(종료: 빈칸): ")
    if content == "":
        break
    else:
        f.write(content + "\n")
f.close()