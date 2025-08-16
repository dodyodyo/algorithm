# n: 화폐 종류
# m: 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 m원이 되도록
n, m = map(int, input().split())

# n개의 화폐 가치(단위)정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 (보텀업)
d[0] = 0  # 0원을 만들기 위한 최소한의 하폐개수 0개
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
