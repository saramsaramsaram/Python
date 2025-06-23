class memberInfo:
    def __init__(self, idx, password, name):
        self.idx = idx
        self.password = password
        self.name = name
    def getMember(self):
        return f'{self.idx}, {self.password}, {self.name}'
    
my_member = memberInfo('king', "1234", "홍길동")
print(my_member.getMember())