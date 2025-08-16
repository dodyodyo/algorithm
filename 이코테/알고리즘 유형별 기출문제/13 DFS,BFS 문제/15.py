# 그래프에서 모든 간선의 비용이 동일할 때는 BFS를 이용하여 최단 거리를 찾을 수 있다.

from collections import deque


# 최단 거리는 bfs로 푸는 것이 좋음
def bfs(start):
    queue = deque([start])
    distance[start] = 0  # 출발도시이므로 거리가 0
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            # 아지 방문하지 않은 도시라면
            if distance[next] == -1:
                queue.append(next)
                distance[next] = distance[now] + 1


# 도시의 개수 N, 도로의 개수 M,  거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())

# 전역변수로 모든 도로 정보 입력받기
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 거리 초기화  방문하지 않음 == 거리가 -1
distance = [-1] * (n + 1)

bfs(x)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)


# -----------------------------------------------------------------


# DFS로 최단 거리 찾기 (비효율적)
def dfs(now, dist):
    # 현재 도시까지의 거리가 이미 알려진 거리보다 크면 탐색 중단
    if distance[now] < dist:
        return

    # 현재 도시까지의 거리가 더 짧다면 갱신
    distance[now] = dist

    # 인접한 도시로 재귀적으로 이동
    for next in graph[now]:
        if distance[next] == -1 or distance[next] > dist + 1:
            dfs(next, dist + 1)


# 도시의 개수 N, 도로의 개수 M,  거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())

# 전역변수로 모든 도로 정보 입력받기
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 거리 초기화 (방문하지 않음 == 거리가 -1)
distance = [-1] * (n + 1)

# DFS 탐색 시작
dfs(x, 0)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if not check:
    print(-1)
