# Day 2: 사용자 입력과 간단한 조건문

# 사용자에게 이름을 입력받는다
name = input("당신의 이름은 무엇인가요? ")
print("안녕하세요, " + name + "님!")

# 나이를 입력받아서 정수형으로 변환
age = int(input("몇 살이신가요? "))
if age >= 20:
    print("성인이시네요!")
else:
    print("아직 미성년자시네요!")

# 숫자를 입력받고 홀수인지 짝수인지 판단
num = int(input("숫자를 입력해주세요: "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
