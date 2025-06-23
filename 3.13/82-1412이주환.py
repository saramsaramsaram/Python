with open*("attendance.txt", "w") as f:
    for i in range(5):
        name = input("이름을 입력하세요: ")
        f.write(name + "\n")