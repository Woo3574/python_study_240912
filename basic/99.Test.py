'''
year = "2024"
month = "09"
day = "11"
hour = "08"
min = "49"

print(f"{year}",f"{month}",f"{day}",sep= "-")
print(f"{hour}",f"{min}",sep= ":")

hour = int(input("현재 몇 시 :"))
min = int(input("현재 몇 분 :"))

print(f"현재시간은{hour}시{min}분 입니다.")
'''
"""
# 24시간제 시간을 : 기준으로 입력 받아서 시,분,초로 찍는데 12시간제로 변환

hour,min,sec = map(int,input("몇시 몇분 몇초 :").split(":"))
if hour > 12:
    hour -=12
    print(f"{hour}시{min}분{sec}초")
else:
    print(f"{hour}시{min}분{sec}초")
"""
"""
kim = True
tae = 1
woo = "밥먹었어?"

print(type(kim))
print(type(tae))
print(type(woo))
"""
"""
# 주민등록번호 뒷자리의 수에따라 해당 주민등록번호 숫자가 남성인지 여성인지 표현하시오 (940429-1234567)
born_num = input("주민등록번호 : ")
gender = born_num[7]
if gender == '1' or gender == '3':
    print("남성입니다")
elif gender == '2' or gender == '4':
    print("여성입니다")
else:
    print("잘못입력하셨습니다")
"""
'''
#뒷 자리 주민등록번호를 가지고 1900년생인지 2000년생인지 확인하시오(xx0429-4123456)
born_num = input("주민등록번호 : ")
gender = born_num[7]
age1 = '90'
if gender == '1' or gender == '2':
    print(f"19{age1}년생입니다")
elif gender == '3' or gender == '4':
    print("2000년생입니다")
else:
    print("잘못된 정보를 입력하셨습니다")
'''

####### (2-1)입출력
'''
name = input("이름을 입력하세요. : ")
age = int(input("나이를 입력하세요. : "))

print(f"{name}",f"{age}")
print(f"{name}",f"{age}", sep='\n')
print(f"{name}",f"{age}", sep='\t')
print(f"{name}",f"{age}", sep='\b')
print(f"{name}",f"{age}", sep='\r')
'''
####### (3-1)입력예제
'''
name = input("이름을 입력하세요 : ")
age = input("나이를 입력하세요 : ")
job = input("직업을 입력하세요 : ")
score = float(input("성적을 입력하세요 : "))

print(f"{name} {age} {job} {score:.4f}")
'''
####### (3-2)입력예제
'''
#아래 학생의 4과목 총점을 구한다음 평균 점수을 구해보시오
#국어 82점,영어 45점,수학 57점,과학 78점

kor,eng,math,scn = map(int,input ("성적을 순서대로 입력하시오 : ").split())
print(f"총점 : {kor+eng+math+scn} ")
print(f"평균 : {(kor+eng+math+scn)/4} ")
'''
import time

for i in range(1, 101):
    time.sleep(0.1)
    print(f"\r{i}%",end="")