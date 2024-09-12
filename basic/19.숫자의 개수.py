# 자연수 A, B, C
# A = 150, B = 266, C =427 이라면 A * B * C = 150 * 266 * 427 = 17037300
# 3 = 0이 3개
# 1 = 1이 1개
# 0
# 2 = 4가 2개
# 0
# 0
# 2 = 7이 2개
# 0
# 0
# 등장하는 숫자(0~9)의 개수를 세는 문제 :
# 범위 기반 for문 사용, count("찾고자 하는 문자")
'''
a, b, c = map(int, input("정수 입력 : ").split()) # 숫자를 공백 기준으로 입력 받음
print(a * b * c)
total = str(a * b * c)
for i in range(10): # 0~9
    print(total.count(str(i)),end = " ")
'''

# 실습 2번 : 문자열 반전, 문자열을 입력 받아서 문자열 반전 출력
# ex) ABCDEF => FEDCBA
#    A B C D E F
#    0 1 2 3 4 5 (range 시작값은 0)
# -1 0 1 2 3 4 5 (범위 하나를 눌려주는것)
'''
in_str = input("문자열 입력 : ")
for i in range(len(in_str)-1,-1,-1):
    print(in_str[i], end="")

in_str = input("문자열 입력 : ")
reverse_str = in_str[::-1]
print(reverse_str)
'''
# 입력 : 5
# *
# **
# ***
# ****
# *****
'''
n = int(input("정수 입력 : "))
sta = str("*")

for i in range(n): # 행의 개수
    for j in range(i+1): # 별의 개수
     print("*", end="")
    print()
'''