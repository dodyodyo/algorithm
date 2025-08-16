# 데이터의 개수가 1,000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이상이라면
# input()함수를 사용하지 말고 readline()함수를 이용하면 시간초과를 피할 수 있다.

# 하나의 문자열 데이터 입력받기
# sys 라이브러리를 사용할 때는 한 줄 입력박고 나서 rstrip()함수를 사용해야됨
# why? readline()으로 입력하면 엔터가 줄 바꿈 기호로 입력됨 -> rstrip()함수가 줄 바꿈 기호 제거
import sys

input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data)
