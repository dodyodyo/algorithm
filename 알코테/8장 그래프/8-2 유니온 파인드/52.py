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


def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False


N, M = map(int, input().split())  # 사람수, 파티 개수
trueP = list(map(int, input().split()))  # 진실을 아는 사람 데이터
T = trueP[0]  # 진실을 아는 사람의 수
del trueP[0]  # 진실을 아는 사람의 수 지우기
result = 0
party = [[] for _ in range(M)]

for i in range(M):
    party[i] = list(map(int, input().split()))
    del party[i][0]  # 파티에 오는 사람의 수

# 대표 노드를 자기 노드로 초기화
parent = [0] * (N + 1)
for i in range(N + 1):
    parent[i] = i

# 각 파티에 참여한 사람들을 1개의 그룹으로 만들기
for i in range(M):
    firstPeople = party[i][0]
    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])

# 각 파티의 대표 노드와 진실을 아는 사람들의 대표 노득가 같다면 과장할 수 없음
for i in range(M):
    isPossible = True
    # 파티 사람 노드는 모두 연결돼 있으므로 아무 사람이나 지정해 find연산을 수행
    firstPeople = party[i][0]
    for j in range(len(trueP)):
        if find(firstPeople) == find(trueP[j]):
            isPossible = False
            break
    if isPossible:
        result += 1

print(result)
