from copy import deepcopy
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    temp[sx][sy] = -1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = -1
                    q.append((nx, ny))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

highest = max(map(max, board))
max_value = 1  # 아무 지역도 물에 잠기지 않으며 안전지역의 개수는 1
for height in range(1, highest + 1):
    cnt = 0
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] <= height:
                temp[i][j] = -1
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 0:
                bfs(i, j)
                cnt += 1
    if cnt > max_value:
        max_value = cnt

print(max_value)
