# 표준 입출력 : 콘솔 입출력을 의미
# [] 대괄호 : 리스트를 표시
# {} 중괄호 : 딕셔너리 표시
# () 소괄호 : 함수의 인수,튜플


# print() : 화면 출력을 위한 함수
print(36)
print('문자열')
print([1,2,3]) # 리스트 출력
print('파'+'이'+'썬') # + 문자열을 이어주는 연산
print('파','이','썬', sep=' ') # , (콤마) 구분자를 의미, 구분자의 기본 값을 공백 sep
print('파''이''썬')

year = 2024
month = 9
day = 10
#print(f"{year}",f"{month}",f"{day}",sep ="-") # sep = 세퍼레이트 콤마의 구분자 문자열을 바꿀수있음* 기본적으로 뒤에 적용됨 end도
print(f"{year}",f"{month}",f"{day}",sep ="-")
# 이스케이프 문자 : 출력 구간의 흐름을 제어
# \n(줄바꿈), \t(탭을 의미), \b(백스페이스), \r(커서를 맨 앞으로 돌림)

print('\n\n', sep='', end='\n') # sep,end는 기본식
print('Banana\b')
print('Banana\rApple')
import time
for i in range(1, 101):
   time.sleep(1)
 print(f'\r{i}%',end='')

#출력 스타일 정리
name = "김태우"
age = 30
gender = '남성'
job = '개발자'
addr = '경기도 광명시 하안동'

#서식지정자 스타일 (C언어 방법)
print("======= 서식 지정자 스타일 =======")
print('이름 : %s 성별 : %s'%(name,gender))
print('나이 : %d'%age)
print('주속 : %s'%addr)

#파이썬 old 스타일
print('====== 파이썬 OLD 스타일 ======')
print('이름 : {} 성별 : {}'.format(name,gender))
print('주소 : {}'.format(addr))

#파이썬의 현재 스타일
print('====== 파이썬 현재 스타일 ======')
print(f'이름 : {name} 성별 : {gender}')
print(f'주소 : {addr}')

#문자열 연결 연산자 사용 방식
print('이름 :' + name)
print('나이 :' + str(age))

#정렬
num1 = 10
num2 = 100
num3 = 1000
num4 = 10000
num5 = 3.14592945844509804586045968

print(f'|{num1:8}|')
print(f'|{num2:8}|')
print(f'|{num3:8}|')
print(f'|{num4:8}|')
print(f'{num5}')

print(f'|{num1:<8}|')
print(f'|{num2:<8}|')
print(f'|{num3:<8}|')
print(f'|{num4:<8}|')
print(f'{num5:.2f}')

print(f'|{num1:^8}|')
print(f'|{num2:^8}|')
print(f'|{num3:^8}|')
print(f'|{num4:^8}|')
print(f'{num5:.3f}')