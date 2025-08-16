from itertools import combinations
from collections import deque
from copy import deepcopy

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

INF = int(1e9)


def virus_time():
    max_value = -1
    for i in range(n):
        for j in range(n):
            if temp[i][j] != '-' and temp[i][j] != '*' and temp[i][j] != -1:
                if temp[i][j] > max_value:
                    max_value = temp[i][j]
    return max_value


def is_blank(x, y):
    q = deque([(x, y)])
    visited = [(x, y)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                if temp[nx][ny] == '*':
                    q.append((nx, ny))
                    visited.append((nx, ny))
                elif temp[nx][ny] == -1:
                    return True
    return False


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
            distance[i][j] = '*'
            virusSet.append((i, j))

min_time = INF
process = False
for virus in combinations(virusSet, m):
    temp = deepcopy(distance)
    q = deque()
    for vx, vy in virus:  # 비활성된 바이러스 m개를 활성화시킴
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

                if temp[nx][ny] == '*' and is_blank(nx,ny):
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
