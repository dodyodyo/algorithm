from collections import deque

# 동, 서, 남, 북, 위, 아래
dz = [0, 0, 0, 0, -1, 1]
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]


def bfs(start, finish):
    dist = [[[-1] * c for _ in range(r)] for _ in range(l)]

    q = deque([start])
    dist[start[0]][start[1]][start[2]] = 0
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and 0 <= nz < l:
                if dist[nz][nx][ny] == -1 and board[nz][nx][ny] != '#':
                    q.append((nz, nx, ny))
                    dist[nz][nx][ny] = dist[z][x][y] + 1
    if dist[finish[0]][finish[1]][finish[2]] != -1:
        print("Escaped in {0} minute(s).".format(dist[finish[0]][finish[1]][finish[2]]))
    else:
        print("Trapped!")


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    board = []
    for _ in range(l):
        board.append([list(input()) for _ in range(r)])
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if board[i][j][k] == 'S':
                    start = (i, j, k)
                if board[i][j][k] == 'E':
                    finish = (i, j, k)
    bfs(start, finish)
