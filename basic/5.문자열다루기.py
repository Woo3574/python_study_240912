#문자열이란? 문자로 이루어진 데이터의 집합
#"",'',""" """,''' '''
#인덱싱 : 시퀀스(리스트, 튜플, 문자열, )input() 자료형에서 특정위치의 요소를 선택하는 작업
#인덱싱은 0 부터 시작
#슬라이싱 : 시퀀스 자료형에서 일부 데이터를 추출하는 것 [스타트지점:엔드지점]
########################
'''
born_num = input("주민등록번호 입력 : ") # 940429-1234567

#인덱싱
gender = born_num[7] #gender = 성별
if gender == "1" or gender == "3": #1900년생 뒷자리 첫번째는 1,2 2000년생 뒷자리 첫번째는 3,4
    print("남성입니다")
else:
    print("여성입니다")

#태어난 년도를 구하기 위해서 슬라이싱
born_year = born_num[:2] # 0에서 2미만,0에서 부터 시작 되는 경우는 생략 가능
born_year = int(born_year)
if gender == "1" or gender == "2":
    born_year +=1900
else: born_year +=2000

print(f"태어난 년도:{born_year}")

#생일 출력 : 0720 => 7월 20일 (예제)
month = born_num[2:4]
day = born_num[4:6]
month = int(month)
day = int(day)

#생년월일
print("생년월일 : "+born_num[:6]) # 940429-1234567
print("뒤 7자리 : "+born_num[7:]) # 7에서 끝까지
print("뒤 7자리 : "+born_num[-7:]) # -1은 맨뒤자리

#print(born_num[14]) # string index out of range

life = "Life is too short,You need Python"
tmp = life[0]+life[1]+life[2]+life[3] #리터럴 상수(대입을해버린 값)박제되는것은 변수로 값을 변경할수없다
print(tmp)

#life[0] = "l" #리터럴 상수(대입을해버린 값)박제되는것은 변수로 값을 변경할수없다(컴파일할때 박제됨 위에서 사용 tmp에대입)

#대소문자 바꾸기 : upper(), lower()
a = "Hello Python Program..."
print(a.upper())
print(a.lower())
#대문자는 소문자로 소문자는 대문자로... (예제)
'''
########################

#문자열 변경 : replace("기존 문자열",("바꿀 문자열")
b = "Hello Python Program..."
n_b = b.replace("Python ","JavaScript")
print(n_b)

#문자열에 포함된 문자 갯수 세기 및 문자열 길이 구하기
#count(): 문자열 내장 메서드로 문자열에 포함된 문자의 갯수를 반환
#__len__() : 문자열 길이를 반환
#len() : 문자열 길이를 반환

c = "Hello Python Program..."
print(c.count("l")) #해당 문자열에서 매개 변수로 전달한 문자/문자열 갯수를 반환
print(len(c)) # 문자열 길이 반환
print(c.__len__()) # 문자열 길이 반환

#문자열 찾기 : find(),rfind(),index()
#fint() : 찾은 문자열의 시작 인덱스 반환, 찾지 못하면 -1
#index() : 찾은 문자열의 시작 인덱스 반환, 찾지 못하면 ValueError 발생하고 종료됨
#rfind() : 뒤에서 부터 문자열을 찾음, 찾은 문자열의 인덱스는 앞에서 부터 계산
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기,가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))

print(phrase.find("나에게"))
print(phrase.rfind("나에게"))
new_phrase = phrase.replace("가장","나에게")
print(new_phrase)

#문자열 연산자 : +,*
def sum_ex(x,y):
    return x + y
print(sum_ex(100,200))
print(sum_ex(3.14,5.88))
print(sum_ex("KOREA","SEOUL"))

print("태양고"+"나희도")
print("!"*10)
list = [0]*10
print(list)

#문자열 양옆의 공백제거 : strip()
d = """
       안녕하세요.
       문자열의 공백을 제거하겠습니다.
       네네네....                
"""
print(d.strip())
