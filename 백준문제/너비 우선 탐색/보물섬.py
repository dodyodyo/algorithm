from collections import deque

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(sx, sy):
    dist = [[-1] * m for _ in range(n)]
    q = deque([(sx, sy)])
    dist[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1 and board[nx][ny] == 'L':
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    return dist


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

result = -1
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            dist = bfs(i, j)
            if max(map(max, dist)) > result:
                result = max(map(max, dist))
print(result)
