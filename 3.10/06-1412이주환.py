won = int(input("예금 금액(원) : "))
rate = float(input("예금 이율(%) : "))
year = int(input("예금 기간(년) : "))
print("#" * 20)

print(f'{won}원을 {rate}% 이율로 {year}년간 예치 후 원리 합계는 {int(won + (won * rate * 0.01 * year))}원')