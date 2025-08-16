# 백준 알고스팟 문제와 거의 동일 dfs, bfs, 다익스트라모두 풀 수 있음
# dfs bfs 다익스트라로 풀수 있는 정말 중요한 문제
import sys
from collections import deque

INF = int(1e9)
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    q = deque([(0, 0, 0)])  # (0,0)과 (N-1,N-1)은 항상 뚫려있다.
    visited[0][0] = True
    while q:
        x, y, sum = q.popleft()
        if x == n - 1 and y == n - 1:
            print(sum)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == 1:
                    q.appendleft((nx, ny, sum))
                if board[nx][ny] == 0:
                    q.append((nx, ny, sum + 1))
                visited[nx][ny] = True


n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
bfs()
