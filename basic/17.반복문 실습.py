# 양의 정수 n을 입력 받아 n * n 크기의 행렬을 출력하는 프로그램을 작성
# 이 때 행렬의 값은 1부터 시작하여 왼쪽에서 오른쪽, 위에서 아래 순서대로 채워 넣음.
# 입력 : 4
#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16

# 1. 입력 받은 값으로 실제 출력 범위를 정해야 함
# 2. 줄바꿈에 대하 처리
# 3. 줄맞춤
'''
n = int(input("정수 입력 : "))
for i in range(1,n * n +1):    # i는 출력값 1은 시작값, n * n +1 는 출력 범위값
    print(f"|{i:6}|", end=" ") #|| 표기하기위해서 넣어논것(지워도 식에 문제는 없음)
    if i % n == 0: print()
'''
#######
# 이중 for 문 사용하기
'''
n = int(input("정수 입력 : "))
for i in range(n): # 0 ~ n 미만까지
    print(f"i={i} ", end="")
    for j in range(n):
        print("*", end=" ")
    print()
'''
'''
# 이중 for문 구구단 찍기
for i in range(2, 10): # 2단 ~ 9단
    for j in range(1, 10):
        print(f"{i} X {j} = {i * j}")
    print("-"*20)
'''
#######
# 제어문 : break, continue
# break : 반복문을 탈출 할 때 사용
# continue : 아래의 문장을 수행하지 않고 반복문의 조건식으로 이동, (해당 루틴은 수행된걸로 간주)
'''
n = int(input("정수 입력 : "))
for i in range(1, n+3 ):
    if i % 2 == 0: continue
    print(i, end="-")
'''
#######
# 반복문을 반대로 수행하기
'''
n = int(input("정수 입력 : "))
for i in range(n, 0 - 1, -1): # 시작값, 최종값, 증감값
    print(f"인덱스 : {i}")
'''
# for문으로 알파벳 출력 하기
# ASCII
# chr() : 유니코드를 입력 받아 그 코드에 해당하는 문자를 출력
# ord() : 문자의 유니코드 값을 돌려주는 함수

for i in range(ord("A"),ord("z")+1):
    print(chr(i), end=" ")
print()

for i in range(65,91): # A:65 Z:90
    print(chr(i), end=" ")
print()