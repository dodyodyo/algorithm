from collections import deque

# 동: 0, 남: 1, 서: 2, 북: 3
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice = [0, 1, 2, 3, 4, 5, 6]  # 0번 인덱스는 사용x


# 동: 0, 남: 1, 서: 2, 북: 3
def rolling(order):
    if order == 0:
        dice[6], dice[3], dice[1], dice[4] = dice[3], dice[1], dice[4], dice[6]
    elif order == 1:
        dice[6], dice[5], dice[1], dice[2] = dice[5], dice[1], dice[2], dice[6]
    elif order == 2:
        dice[6], dice[4], dice[1], dice[3] = dice[4], dice[1], dice[3], dice[6]
    elif order == 3:
        dice[6], dice[2], dice[1], dice[5] = dice[2], dice[1], dice[5], dice[6]


# 보드 N x M 크기
def score(sx, sy):
    visited = [[False] * m for _ in range(n)]
    b = board[sx][sy]
    c = 0

    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        c += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] == b:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return c * b


def rotation():
    global dir
    A, B = dice[6], board[x][y]
    if A > B:
        dir = (dir + 1) % 4
    elif A < B:
        dir = (dir - 1) % 4


x, y = 0, 0  # 보드에 맞게 좌표 수정
dir = 0  # 처음 방향 동쪽
result = 0

for _ in range(k):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not (0 <= nx < n and 0 <= ny < m):
        dir = (dir + 2) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
    x, y = nx, ny
    rolling(dir)
    result += score(x, y)
    rotation()

print(result)
