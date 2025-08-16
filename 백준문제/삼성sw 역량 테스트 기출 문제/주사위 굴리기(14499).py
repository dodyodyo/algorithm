# 지도의 세로 크기 N, 가로 크기 M, 주사위를 놓는 곳의 좌표 x,y, 명령의 개수 K
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]  # 지도
dice = [0] * 7
order = list(map(int, input().split()))  # 이동하는 명령 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

for i in range(k): # k번의 명령
    if order[i] == 1:
        y += 1
        if not (0 <= x < n and 0 <= y < m):
            y -= 1
            continue
        dice[6], dice[3], dice[1], dice[4] = dice[3], dice[1], dice[4], dice[6]  # 튜플 언패킹 사용
        if board[x][y] == 0:  # 이동한 칸에 적혀있는 수가 0일때
            board[x][y] = dice[6]  # 바닥면에 쓰여 있는 수를 칸에 복사
        else:  # 이동한 칸에 적혀있는 수가 0이 아닐 때
            dice[6] = board[x][y]  # 칸에 쓰여있는 수가 주사위의 바닥면으로 복사
            board[x][y] = 0  # 칸에 적혀 있는 수는 0이 된다

    elif order[i] == 2:
        y -= 1
        if not (0 <= x < n and 0 <= y < m):
            y += 1
            continue
        dice[6], dice[4], dice[1], dice[3] = dice[4], dice[1], dice[3], dice[6]
        if board[x][y] == 0:
            board[x][y] = dice[6]
        else:
            dice[6] = board[x][y]
            board[x][y] = 0

    elif order[i] == 3:
        x -= 1
        if not (0 <= x < n and 0 <= y < m):
            x += 1
            continue
        dice[6], dice[2], dice[1], dice[5] = dice[2], dice[1], dice[5], dice[6]
        if board[x][y] == 0:
            board[x][y] = dice[6]
        else:
            dice[6] = board[x][y]
            board[x][y] = 0

    elif order[i] == 4:
        x += 1
        if not (0 <= x < n and 0 <= y < m):
            x -= 1
            continue
        dice[6], dice[5], dice[1], dice[2] = dice[5], dice[1], dice[2], dice[6]
        if board[x][y] == 0:
            board[x][y] = dice[6]
        else:
            dice[6] = board[x][y]
            board[x][y] = 0
    print(dice[1])
