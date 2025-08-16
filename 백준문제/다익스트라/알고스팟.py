# dfs bfs 다익스트라로 풀수 있는 정말 중요한 문제
import sys
from collections import deque

INF = int(1e9)
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    q = deque([(0, 0, 0)])  # (0,0)과 (N-1,M-1)은 항상 뚫려있다.
    visited[0][0] = True
    while q:
        x, y, sum = q.popleft()
        if x == n - 1 and y == m - 1:
            print(sum)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    q.appendleft((nx, ny, sum))
                if board[nx][ny] == 1:
                    q.append((nx, ny, sum + 1))
                visited[nx][ny] = True


# 가로 크기: M, 세로 크기: N
m, n = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
bfs()
# -------------------------------------------------------------------------

import heapq
import sys

INF = int(1e9)
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 가로 크기: M, 세로 크기: N
m, n = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
distance = [[INF] * m for _ in range(n)]


def dijkstra():
    q = []
    distance[0][0] = 0
    heapq.heappush(q, (0, 0, 0))
    while q:
        nowDist, nowx, nowy = heapq.heappop(q)
        if distance[nowx][nowy] < nowDist:
            continue
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if 0 <= nextx < n and 0 <= nexty < m:
                cost = nowDist + board[nextx][nexty]
                if cost < distance[nextx][nexty]:
                    distance[nextx][nexty] = cost
                    heapq.heappush(q, (cost, nextx, nexty))
    

dijkstra()
print(distance[n - 1][m - 1])
