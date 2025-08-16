from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def move(x, y, i):
    cnt = 0
    while board[x][y] != '#' and board[x][y] != 'O':
        x += dx[i]
        y += dy[i]
        cnt += 1
    return x, y, cnt


n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
            
visited = []
q = deque([(rx, ry, bx, by, 0)])
visited.append((rx, ry, bx, by))
while q:
    rx, ry, bx, by, result = q.popleft()
    if result > 10:
        print(-1)
        break
    for i in range(4):
        nrx, nry, rcnt = move(rx, ry, i)
        nbx, nby, bcnt = move(bx, by, i)

        if board[nbx][nby] == 'O':
            continue

        if board[nrx][nry] == 'O':
            print(result)
            break

        if nrx == nbx and nry == nby:
            if rcnt > bcnt:
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]

        if (nrx, nry, nbx, nby) not in visited:
            q.append((nrx, nry, nbx, nby, result + 1))
            visited.append((nrx, nry, nbx, nby))
