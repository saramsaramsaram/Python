print("#" * 20)
print("  BMI 계산 프로그램")
print("#" * 20)
a = float(input("키(cm) : "))
b = float(input("몸무게(kg) : "))
print("#" * 20)
print(f'당신의 BMI 지수는 {b/(a/100)**2: .1f} 입니다.')