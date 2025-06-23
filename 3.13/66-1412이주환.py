class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def introduce(self):
        print(f"안녕하세요, 제 이름은 {self.name}이고, 학년은 {self.grade}입니다.")

s1 = Student("홍길동", 3)
s1.introduce()
s2 = Student("이순신", 4)
s2.introduce()