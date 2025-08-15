"""
DFS: 깊이 우선 탐색 알고리즘
특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 
다시 돌아가 다른 경로로 탐색하는 알고리즘
스택으로 구현 or 재귀함수로 구현

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 
방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

인접 노드가 여러개일 때는 보통 노드 번호가 가장 작은 노드를 우선한다.
"""


# DFS
def dfs(v):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for next in graph[v]:
        if not visited[next]:
            dfs(next)


# 각 노드가 연결된 정보를 리스트로 표현
graph = [[], [2, 3], [5, 6], [4], [6], [], []]

# 각 노드가 방문된 정보르르 리스트로 표현
visited = [False] * 7
dfs(1)

"""
BFS: 너비 우선 탐색 알고리즘
그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
큐 자료구조 이요
모든 간선의 비용이 1일때 최단 거리를 찾을 수 잇다.
모든 간선의 비용이 다르고 양수일때는 다익스트라, 플로이드워셜 알고리즘일 이용해야 한다.

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2.큐에서 노드를 꺼낸 뒤에 해당 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

"""
# BFS
from collections import deque


def bfs(start):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        now = queue.popleft()
        print(now, end=' ')
        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True


# 각 노드가 연결된 정보를 리스트로 표현
graph = [[], [2, 3], [5, 6], [4], [6], [], []]

# 각 노드가 방문된 정보르르 리스트로 표현
visited = [False] * (6 + 1)
bfs(1)


# ------------------------------------------------------
from collections import deque

# N x N 크기의 보드에서 bfs 구조
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def bfs(sx, sy):
    visited = [[False] * n for _ in range(n)]
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        print(x, y, end=' ')
        for i in range(n):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True


# --------------------------------------------------------------------
# bfs를 쓸때 visited와 dist를 쓰지 말고 dist만 쓰면 메모리 활용 올라감
# dist가 -1: 방문하지 않은 곳


# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


# dist: -1: 방문 x dist: 0 방문 O 라 할때
def bfs(sx, sy):
    dist = [[-1] * n for _ in range(n)]
    q = deque([(sx, sy)])
    dist[sx][sy] = 0
    while q:
        x, y = q.popleft()
        print(x, y, end=' ')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1:  # 다른 조건이 있으면 추가
                    q.append((nx, ny))
                    dist[nx][ny] = 0
