from collections import deque

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수
board = [[0] * (n + 1) for _ in range(n + 1)]  # 맵 정보

# 사과가 있는 곳 1
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

dx = [0, 1, 0, -1]  # 동, 남, 서, 북
dy = [1, 0, -1, 0]
direction = 0  # 처음 방향 동쪽
info = []  # 방향 회전 저장
index = 0  # 방향 변수

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

time = 0  # 시간
q = deque()
x, y = 1, 1
board[x][y] = 2  # 지렁이가 있는 곳 2로 표현
q.append((x, y))  # 큐에 처음 지렁이 위치 저장

while True:
    if index < l and time == info[index][0]:
        if info[index][1] == "D":  # 시계방향 90도 회전
            direction = (direction + 1) % 4
        if info[index][1] == "L":  # 반시계방향 90도 회전
            direction = (direction - 1) % 4
        index += 1
        continue

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 뱀이 벽과 자기자신에 부딪히지 않을 때
    if nx >= 1 and nx <= n and ny >= 1 and ny <= n and board[nx][ny] != 2:
        # 사과가 없다면
        if board[nx][ny] == 0:
            q.append((nx, ny))
            tx, ty = q.popleft()
            board[nx][ny] = 2
            board[tx][ty] = 0

        # 사과가 있다면
        if board[nx][ny] == 1:
            q.append((nx, ny))
            board[nx][ny] = 2

    # 뱀이 벽과 자기자신에 부딪힐 때
    else:
        time += 1
        print(time)
        break
    x, y = nx, ny
    time += 1
