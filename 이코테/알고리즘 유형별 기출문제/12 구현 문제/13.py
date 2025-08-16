from itertools import combinations

n, m = map(int, input().split())

house, chicken = [], []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        if data[j] == 2:
            chicken.append((i, j))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 개수
candidates = list(combinations(chicken, m))

cityChickenDistance = 1e9
for candidate in candidates:
    chickenDistance = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        chickenDistance += temp
    cityChickenDistance = min(cityChickenDistance, chickenDistance)

print(cityChickenDistance)
