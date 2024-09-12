# 프로그램에서 값을 연산해야 하는 경우 사용
# 산술연산자 : +,-,*,/,//(몫),%(나머지),**  ## //<-[데이터 타입이 없기때문에 몫을 구하는 연산자가 필요함] % <-[몫을 구하고난 *나머지*]
'''
i= 10
j = 3
print(i + j)
print(i - j)
print(i * j)
print(i / j)
print(i // j) # 몫을 구한다 10//3 3-1 몫은 3 파이썬만있음(연산자)
print(i % j)  # 나머지를 구한다 10//3 3-1 나머지 1, 알고리즘 문제를 풀기위해서 많이 사용
print(i ** j) # 10^3 파이썬만있음(연산자)

TAX_RATE = 0.10 # 세율 (대문자는 고정댄 값을 표시)
income = int(input("당신의 수입은 얼마 입니까?"))
print(f"당신이 내야 할 세금은 {income*TAX_RATE}")
'''
##########
#대입 연산자 : 값을 변수에 대입
#대입 연산자의 종류 : =, +=, =+, *=, /=, %=, [{!=} ->(not =) ex) a != 10 a와 10이 같지않으면]
'''
num1 = 10
num1 += 2 #num1 = num1 +2
print(num1) #12
num1 -= 10
print(num1) #2
num1 *= 2
print(num1)
'''
##########
# 비교 연산자 : 두개의 값을 비교해서 참/거짓을 만들어 냄
# == 같다, > 왼쪽이 크다, >= 왼쪽이 크거나 같다, <, <=
'''
a = 10
b = 20
print( a > b ) #False
print( a < b ) #True
print( a == b ) #False
print( a >= b ) #False
print( a <= b ) #True
'''
##########
# 관계 연산자 : and(java &&) 둘다 참이어야 참, or(||) 둘중 하나만 참이면 참, not(!) 이전 상태를 반전
'''
x = 10
y = 20
z = 30
rst1 = (x > 0) and (x > y) # False
rst2 = (x > 0) or (x > y) # True
rst3 = not((x > 0) and (x > y)) # True
print(rst1,rst2,rst3)
'''
######
# 3항 연산자 : 항이 3개인 연산자 : 참과 거짓이 있는 조건문 동일 (조건문) if-else ,3항 연산자
'''
age = int(input("나이를 입력하세요"))
is_adult = age > 19 and "성인" or "미성년자"
print(f"당신은 {is_adult}입니다.")
'''
'''
age = int(input("나이를 입력하세요"))
if age > 19:
    print("당신은 성인 입니다")
else:
    print("당신은 미성년자 입니다")
'''
'''
age = int(input("나이를 입력하세요"))
is_adult = True if age > 18 else False
print(1) if age > 18 else print(-1) ## 미완성된 
'''



