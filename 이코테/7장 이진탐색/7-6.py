n = int(input())
array = [0] * 1000001

# 가게에 있느 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1  # i는 문자열로 입력받았으므로

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
