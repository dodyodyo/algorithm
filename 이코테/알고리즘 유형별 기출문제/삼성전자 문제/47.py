import copy


def move_all_fishes(board, now_x, now_y):
    for fish in range(1, 17):
        position = None
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == fish:
                    position = (i, j)

        if position != None:
            x, y = position[0], position[1]
            direction = board[x][y][1]
            for i in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]

                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        board[x][y][1] = direction
                        board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                        break
                direction = (direction + 1) % 8


def eat_possible_position(board, now_x, now_y):
    positions = []
    direction = board[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]

        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if board[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
        else:
            return positions


result = 0


def dfs(board, now_x, now_y, total):
    global result
    board = copy.deepcopy(board)

    total += board[now_x][now_y][0]  # 현재 위치의 물고기 먹기
    board[now_x][now_y][0] = -1  # 물고기를 먹었으므로 번호 값을 1로 변환
    move_all_fishes(board, now_x, now_y)
    positions = eat_possible_position(board, now_x, now_y)

    if len(positions) == 0:
        result = max(result, total)
        return
    for x, y in positions:
        dfs(board, x, y, total)


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 물고기가 없으면 -1 물고기가 있으면 해당 번호의 물고기
board = [[-1] * 4 for _ in range(4)]
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = [row[j * 2], row[j * 2 + 1] - 1]


dfs(board, 0, 0, 0)
print(result)
