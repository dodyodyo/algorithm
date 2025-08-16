def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


N = int(input())  # 도시의 수
M = int(input())  # 여행 계획에 속한 도시의 수
dosi = [[0 for j in range(N + 1)] for i in range(N + 1)]  # 도시 연결 데이터 리스트 저장
for i in range(1, N + 1):
    dosi[i] = list(map(int, input().split()))
    dosi[i].insert(0, 0)

# 여행 도시 정보 저장
route = list(map(int, input().split()))
route.insert(0, 0)

# 대표 노드 저장 리스트
parent = [0] * (N + 1)

# 대표 노드를 자기 자신으로 초기화
for i in range(1, N + 1):
    parent[i] = i

# 인접 행렬에서 도시가 연결되어 있으면 unoin 실행
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dosi[i][j] == 1:
            union(i, j)

# 여행 경로에 있는 모든 도시의 대표 도시가 같은지 확인
index = find(route[1])
isConnect = True
for i in range(2, len(route)):
    if index != find(route[i]):
        isConnect = False
        break

if isConnect:
    print("YES")
else:
    print("NO")
