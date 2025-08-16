import sys

input = sys.stdin.readline
data, quiz = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

# 합 배열 만들기
for i in numbers:
    temp += i
    prefix_sum.append(temp)

# 합 배열에서 구간 합 구하기
for _ in range(quiz):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s - 1])
