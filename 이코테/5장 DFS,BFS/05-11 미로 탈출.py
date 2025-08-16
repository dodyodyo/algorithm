"""
# BFS는 시작 시점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색한다.
# BFS는 최단 거리를 구하는데 효과적이다.(물론 DFS로도 풀 수 있음)

from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기(전역변수)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue
            # 괴물인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


# BFS 수행한 결과 출력
print(bfs(0, 0))
"""

"""
# DFS로 구현
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기(전역변수)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# DFS 구현
def dfs(x, y):
    # 현재 위치에서 네 방향으로 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 미로 찾기 공간을 벗어난 경우 무시
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 괴물인 경우 무시
        if graph[nx][ny] == 0:
            continue
        # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            dfs(nx, ny)
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# DFS 수행한 결과 출력
print(dfs(0, 0))
"""
