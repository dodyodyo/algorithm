from itertools import combinations
from collections import deque
from copy import deepcopy

INF = int(1e9)

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def virus_time():
    max_value = -1
    for i in range(n):
        for j in range(n):
            if temp[i][j] != '-' and temp[i][j] != -1:
                if temp[i][j] > max_value:
                    max_value = temp[i][j]
    return max_value


n, m = map(int, input().split())
board = []
virusSet = []
distance = [[-1] * n for _ in range(n)]

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 1:
            distance[i][j] = '-'
        elif board[i][j] == 2:
            virusSet.append((i, j))


min_time = INF
process = False
for viurs in combinations(virusSet, m):
    temp = deepcopy(distance)
    q = deque()
    for vx, vy in viurs:
        temp[vx][vy] = 0
        q.append((vx, vy))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if temp[nx][ny] == '-':
                    continue
                if temp[nx][ny] == -1:
                    temp[nx][ny] = temp[x][y] + 1
                    q.append((nx, ny))

    all_virus = True
    for i in range(n):
        for j in range(n):
            if temp[i][j] == -1:
                all_virus = False

    if all_virus:
        min_time = min(min_time, virus_time())
        process = True

if process:
    print(min_time)
else:
    print(-1)
