# 조건이 참인 동안 반복 수행
'''
n = int(input("정수 입력 : "))
sum = 0 # 값을 누적하기 위한 변수
while n: # while문 0이 아닌 모든 값은 참으로 간주(JAVA 제외)
    sum += n
    n -=1 # n = n -1, [(n--),(n++)파이썬에는 증감연산자가없다]
print(sum)

#들여쓰기 위치 의 차이(print 예를들어 적용)
'''

'''
while n: 
    sum += n
    n -=1 
print(sum)

while n: 
    sum += n
    n -=1 
    print(sum)
'''

'''
n = int(input("정수 입력 : "))
sum = 0
for i in range(1, n+1): # 범위 기반의 for문 (초기 값,미만)
    sum += i
print(sum)
'''

# while문은 주로 횟수가 정해지지 않은 반복적인수행을 할 때 사용 ( 반복문에 빠져나올때 break,exit() )
'''
while True: # 반복문 내에 탈출 조건이 있어야 함
    age = int(input("나이를 입력하세요. : "))
    if 0 <= age <= 200: break # 정상적인 입력이므로 반복문 탈출 (빠져나올수있는 break가 있기때문에 else를 사용하지않아도됨)
    print("나이를 잘 못 입력 하셨습니다.")

print(f"당신의 나이는 {age}살 입니다.")

score = int(input("성적 입력 : "))
'''

'''
while True:
  score = int(input("성적을 입력하세요. : "))
  if 0 <= score <=100:
      if score >=90: print("A")
      elif score >=80: print("B")
      elif score >=70: print("C")
      elif score >=60: print("D")
      else:print("F")
      break
  else:
      print("성적을 잘못 입력 하셨습니다")
'''
#######
# for 문 : 정해진 범위 만큼을 반복 수행 할 때 효과적
# for 요소 in 시퀀스: #시퀀스 자료에 대한 자동 순회, [요소에는 변수값 대입] [시퀀스에 대입할수있는건 (리스트,튜플,문자열,input)]
# for 인덱스 in range(시작값, 종료값, 증감값):

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

name = "anklewnafujibl"
for e in name:
    print(e, end="-")
print() #줄바꿈

for e in input("문자열 입력 : "):
    print(e, end="-")
print()  # 줄바꿈

# for 인덱스 in range(시작값, 종료값, 증감값):
n = int(input("정수 값 입력: "))
sum = 0
for i in range(1, n+1, 1): #시작값이 0인 경우 생략 가능, 증감값이 1인 경우 생략 가능 -> {for i in range(n+1)}
    sum += i
print(sum)
