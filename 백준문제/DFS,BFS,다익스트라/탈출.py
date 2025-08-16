from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(bx, by, gx, gy):
    dist = [[-1] * c for _ in range(r)]

    wq = deque(water)
    bq = deque([(bx, by)])
    dist[bx][by] = 0

    while bq:  # 비버가 탈출할 때까지
        w_cnt = len(wq)
        for _ in range(w_cnt):
            x, y = wq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == '.':  # 유효한 범위이면서 빈공간일때
                    board[nx][ny] = '*'  # 물 범람
                    wq.append((nx, ny))  # 큐에 저장

        b_cnt = len(bq)
        for _ in range(b_cnt):
            x, y = bq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if board[nx][ny] == '.' or board[nx][ny] == 'D':  # 유효한 범위이면서 빈공간일때
                        board[nx][ny] = 'S'  # 비버 이동
                        bq.append((nx, ny))  # 큐에 저장
                        dist[nx][ny] = dist[x][y] + 1
                        if nx == gx and ny ==gy:
                            print(dist[nx][ny])
                            return
    print("KAKTUS")


r, c = map(int, input().split())
water = []

board = [list(input()) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            water.append((i, j))
        elif board[i][j] == 'S':
            bx, by = i, j
        elif board[i][j] == 'D':
            gx, gy = i, j

bfs(bx, by,gx,gy)
