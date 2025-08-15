'''
input() 대신 sys.stdin.readline()을 사용하는 이유
반복문으로 여러줄을 입력 받아야하는 경우 input()으로 입력 받는다면 시간초과가 발생할 수 있다.

'''

'''
strip([chars]): 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거
lstrip([chars]): 인자로 전달된 문자를 String의 왼쪽에서 제거
rstrip([chars]): 인자로 전달된 문자를 String의 오른쪽에서 제거

인자를 전달하지 않으면 String에서 공백을 제거

'''

# # 정수를 받을 때
import sys

a = int(sys.stdin.readline())  # 1엔터
a = int(sys.stdin.readline().rstrip())  # 이것도 가능
print(a)  # 1

a1, a2, a3 = map(int, sys.stdin.readline().split())  # 1 2 3엔터
print(a1, a2, a3)  # 1 2 3

data = list(map(int, sys.stdin.readline().split()))  # 1 2 3엔터
print(data)  # [1, 2, 3]

# 1 3 5엔터4 5 6엔터1 4 8엔터
board = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
print(board)  # [[1, 3, 5], [4, 5, 6], [1, 4, 8]]

# -----------------------------------------------------------
# 문자열을 공백을 기준으로 입력받았을 때
import sys

data = sys.stdin.readline().rstrip()  # a b c엔터
print(data, end='')  # a b c가 data에 저장


# 문자열 n줄을 입력받아 리스트에 저장할 때
import sys

cnt = int(sys.stdin.readline())  # 2엔터
data = [sys.stdin.readline().rstrip() for _ in range(cnt)]  # data1엔터data2엔터
print(data)  # ['data1', 'data2']
# ---------------------------------------------------------------

# rstrip()을 사용하지 않을 때
import sys

cnt = int(sys.stdin.readline())  # 2엔터
data = [sys.stdin.readline() for _ in range(cnt)]  # data1엔터data2엔터
print(data)  # ['data1\n', 'data2\n']

# ---------------------------------------------------
import sys

cnt = int(sys.stdin.readline())  # 2엔터
data = [sys.stdin.readline().split() for _ in range(cnt)]  # a b c엔터d e f엔터
print(data)  # [['a', 'b', 'c'], ['d', 'e', 'f']]
