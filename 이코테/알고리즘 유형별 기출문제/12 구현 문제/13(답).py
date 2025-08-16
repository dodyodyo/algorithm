from itertools import combinations

n, m = map(int, input().split())  # 크기가 n인 도시, 최대 치킨집 개수
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:  # 일반집
            house.append((r, c))
        elif data[c] == 2:  # 치킨 집
            chicken.append((r, c))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))


# 각 집에서 가장 가까운 치킨 거리의 합을 계산하는 함수
# m개의 치킨집 후보 조합하나를 인수로 받음
def get_sum(candidate):
    result = 0  # 치킨 거리의 합
    for hx, hy in house:  # 각각의 모든 집에 대하여
        temp = 1e9
        for cx, cy in candidate:  # 가장 가까운 치킨집과의 거리 구하기
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result


cityChickenDistance = 1e9
for candidate in candidates:
    cityChickenDistance = min(cityChickenDistance, get_sum(candidate))
print(cityChickenDistance)