import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def move(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
            new_board[nx][ny] += board[x][y] // 5
            cnt += 1
    new_board[x][y] += board[x][y] - board[x][y] // 5 * cnt


def up_rotate():
    for i in range(cx - 3, -1, -1):
        board[i + 1][0] = board[i][0]
    for j in range(1, c, 1):
        board[0][j - 1] = board[0][j]
    for i in range(1, cx, 1):
        board[i - 1][c - 1] = board[i][c - 1]
    for j in range(c - 2, 0, -1):
        board[cx - 1][j + 1] = board[cx - 1][j]
    board[cx - 1][1] = 0


def down_rotate():
    for i in range(cx + 2, r, 1):
        board[i - 1][0] = board[i][0]
    for j in range(1, c, 1):
        board[r - 1][j - 1] = board[r - 1][j]
    for i in range(r - 2, cx - 1, -1):
        board[i + 1][c - 1] = board[i][c - 1]
    for j in range(c - 2, 0, -1):
        board[cx][j + 1] = board[cx][j]
    board[cx][1] = 0


def result():
    hap = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] != -1 and board[i][j] != 0:
                hap += board[i][j]
    return hap


r, c, t = map(int, input().split())

board = []
for i in range(r):
    board.append(list(map(int, input().split())))
    if board[i][0] == -1:
        cx = i

for _ in range(t):
    new_board = [[0] * c for _ in range(r)]
    new_board[cx - 1][0] = -1
    new_board[cx][0] = -1

    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                move(i, j)
    board = copy.deepcopy(new_board)

    up_rotate()
    down_rotate()

print(result())
