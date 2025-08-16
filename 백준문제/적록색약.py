from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def differ():
    dist = [[-1] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if dist[i][j] == -1:
                q = deque([(i, j)])
                dist[i][j] = 0
                color = board[i][j]
                cnt += 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if dist[nx][ny] == -1 and board[nx][ny] == color:
                                q.append((nx, ny))
                                dist[nx][ny] = 0
    return cnt


def same():
    dist = [[-1] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if dist[i][j] == -1:
                q = deque([(i, j)])
                dist[i][j] = 0
                color = board[i][j]
                cnt += 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if color == 'R' or color == 'G':
                                if dist[nx][ny] == -1 and (board[nx][ny] == 'R' or board[nx][ny] == 'G'):
                                    q.append((nx, ny))
                                    dist[nx][ny] = 0
                            if color == 'B':
                                if dist[nx][ny] == -1 and board[nx][ny] == 'B':
                                    q.append((nx, ny))
                                    dist[nx][ny] = 0
    return cnt


n = int(input())
board = [list(input()) for _ in range(n)]
print(differ(),same())