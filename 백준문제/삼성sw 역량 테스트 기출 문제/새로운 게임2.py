dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def move():
    game_is_over = False
    for i in range(k):
        x, y, dir = token[i][0], token[i][1], token[i][2]  # 현재 말의 위치와 방향
        # if game[x][y][0] != i + 1:  # 가장 아래에 있는 말만 이동할 수 있다.
        #     continue
        # 다음칸 확인
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:  # 이동하려는 칸이 흰색 일때
            s = game[x][y].index(i + 1)
            game[nx][ny].extend(game[x][y][s:])
            del game[x][y][s:]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:  # 이동하려는 칸이 빨간색일때
            s = game[x][y].index(i + 1)
            game[x][y][s:] = game[x][y][s:][::-1]
            game[nx][ny].extend(game[x][y][s:])
            del game[x][y][s:]
        if (0 <= nx < n and 0 <= ny < n and board[nx][ny] == 2) or not (0 <= nx < n and 0 <= ny < n):  # 이동하려는 칸이 파란색또는 벗어날때
            # 방향을 반대로 하고
            if dir % 2 == 0:
                dir += 1
            else:
                dir -= 1
            # 다음칸 확인
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:  # 이동하려는 칸이 흰색 일때
                s = game[x][y].index(i + 1)
                game[nx][ny].extend(game[x][y][s:])
                del game[x][y][s:]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:  # 이동하려는 칸이 빨간색일때
                s = game[x][y].index(i + 1)
                game[x][y][s:] = game[x][y][s:][::-1]
                game[nx][ny].extend(game[x][y][s:])
                del game[x][y][s:]
            if (0 <= nx < n and 0 <= ny < n and board[nx][ny] == 2) or not (0 <= nx < n and 0 <= ny < n):  # 방향을 반대로 해도 이동하려는 칸이 파란색또는 벗어날때
                nx, ny = x, y  # 방향만 바꾸고 이동하려는 칸 그대로

        for j in game[nx][ny]:  # 위치값 수정
            token[j - 1][0], token[j - 1][1] = nx, ny
        token[i][2] = dir  # 방향값 수정
        if len(game[nx][ny]) >= 4:
            game_is_over = True
            
    return game_is_over


n, k = map(int, input().split())  # 체스판의 크기: N, 말의 개수: K
board = [list(map(int, input().split())) for _ in range(n)]  # 보드의 색을 저장하는 리스트 흰색: 0, 빨간색: 1, 파란색: 2
token = [list(map(int, input().split())) for _ in range(k)]  # 체스말의 행, 열, 이동 방향을 저장하는 리스트
for i in range(k):  # 보드에 맞게 좌표와 방향 수정
    token[i][0] -= 1
    token[i][1] -= 1
    token[i][2] -= 1
game = [[[] for _ in range(n)] for _ in range(n)]  # 보드에서 체스말의 상태(어느 위치에 얼마나쌓여있는지)를 저장하는 리스트

for i in range(k):  # 처음 체스말의 상태
    game[token[i][0]][token[i][1]].append(i + 1)


turn = 0
while True:
    turn += 1
    game_is_over = move()
    if game_is_over or turn > 1000:
        break


if game_is_over:  # 체스가 끝날 수 있을때
    print(turn)
else:  # 체스가 1000턴이 되도록 끝나지 않을 때
    print(-1)
