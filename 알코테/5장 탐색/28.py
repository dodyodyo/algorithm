from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]

# A인접 리스트에 그래프 데이터 저장
for _ in range(N):
    Data = list(map(int, input().split()))
    index = 0
    S = Data[index]
    index += 1
    while True:
        E = Data[index]  # 노드
        if E == -1:
            break
        V = Data[index + 1]  # 가중치
        A[S].append((E, V))
        index += 2

distance = [0] * (N + 1)  # 거리 정보
visited = [False] * (N + 1)  # 방문 정보


# BFS알고리즘 이용
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_node] + i[1]


# BFS수행
BFS(1)

# 거리리스트중 최대값의 인덱스 찾기
maxi = 1
for i in range(2, N + 1):
    if distance[maxi] < distance[i]:
        maxi = i

distance = [0] * (N + 1)
visited = [False] * (N + 1)
BFS(maxi)  # 거꾸로 보면서 처음 노드 뒤에 다른 노드가 있었는 지 확인
print(max(distance))
