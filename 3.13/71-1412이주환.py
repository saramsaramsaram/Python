class BackAccount:
    def __init__(self, acnt):
        self.acnt = acnt
        self.balance = 0
    def deposit(self, amt):
        self.balance += amt
        print(f'{self.acnt} 계좌에 {amt}원이 입금되었습니다.')
    def withdraw(self, amt):
        self.balance -= amt
        print(f'{self.acnt} 계좌에서 {amt}원이 출금되었습니다.')
a = BackAccount('123-456-789')
a.deposit(10000)
a.withdraw(5000)

b = BackAccount('987-654-321')
b.deposit(20000)
b.withdraw(10000)