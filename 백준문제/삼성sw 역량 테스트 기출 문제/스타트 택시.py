from collections import deque
from copy import deepcopy

INF = int(1e9)

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 택시가 승객이 있는 곳까지 움직이고 태운 승객의 번호와, 소모한 연료를 반환하는 함수
def move_passenger(sx, sy):
    temp = deepcopy(board)
    # 벽이 있는 곳은 -1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                temp[i][j] = -1
    visited = [[False] * n for _ in range(n)]  # 방문 여부 기록

    q = deque([(sx, sy)])
    visited[sx][sy] = True  # 시작 위치 방문
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:  # 유효한 범위
                if not visited[nx][ny] and temp[nx][ny] == 0:  # 처음 방문한 곳 + 벽이 아닐때
                    temp[nx][ny] = temp[x][y] + 1
                    q.append((nx, ny))
                    visited[nx][ny] = True

    num, min_dist, min_row, min_col = INF, INF, INF, INF  # 승객 번호, 최소 거리, 최소 행, 최소 열
    for i in range(m):
        if is_passenger[i] and visited[pos[i][0]][pos[i][1]]:  # 승객이 존재하고 승객까지 도착할 수 있을때
            if (temp[pos[i][0]][pos[i][1]] < min_dist) or (temp[pos[i][0]][pos[i][1]] == min_dist and pos[i][0] < min_row) or (temp[pos[i][0]][pos[i][1]] == min_dist and pos[i][0] == min_row and pos[i][1] < min_col):
                min_dist = temp[pos[i][0]][pos[i][1]]
                min_row = pos[i][0]
                min_col = pos[i][1]
                num = i

    # 승객이 있는 곳까지 도달할 수 있을 때
    if num != INF:
        is_passenger[num] = False  # 해당 승객에 대한 서비스 완료
    return num, min_dist


# 승객의 번호를 인수로 받아 택시가 승객을 태우고 목적지까지 소모한 연료와 목적지의 좌표를 반환하는 함수
def move_arrival(num):
    temp = deepcopy(board)
    # 벽이 있는 곳은 -1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                temp[i][j] = -1
    visited = [[False] * n for _ in range(n)]  # 방문 여부 기록

    q = deque([(pos[num][0], pos[num][1])])  # 승객의 시작위치 큐에 삽입
    visited[pos[num][0]][pos[num][1]] = True  # 시작 위치 방문

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:  # 유효한 범위
                if not visited[nx][ny] and temp[nx][ny] == 0:  # 처음 방문한 곳 + 벽이 아닐때
                    temp[nx][ny] = temp[x][y] + 1
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return pos[num][2], pos[num][3], temp[pos[num][2]][pos[num][3]]  # 도착위치 좌표, 소모한 연료


n, m, fuel = map(int, input().split())  # 보드의 크기, 승객의 수, 연료의 양
board = [list(map(int, input().split())) for _ in range(n)]  # 지도
x, y = map(int, input().split())  # 운전을 시작하는 칸의 행, 열 번호
pos = [list(map(int, input().split())) for _ in range(m)]  # 승객의 출발지의 행과 열 번호, 목적지의 행과 열 번호
is_passenger = [True] * m  # 승객을 태웠는지 여부

# 보드에 맞게 좌표 수정
x -= 1
y -= 1
for i in range(m):
    for j in range(4):
        pos[i][j] -= 1

process = True
for _ in range(m):
    # 승객까지 이동
    num, to_passenger_fuel = move_passenger(x, y)
    if to_passenger_fuel == INF:
        process = False
        break

    # 승객을 태우고 도착지까지 이동
    x, y, to_arrival_fuel = move_arrival(num)
    if to_arrival_fuel == 0:
        process = False
        break

    fuel = fuel - to_passenger_fuel - to_arrival_fuel  # 연료 소모
    if fuel < 0:  # 연료가 바닥나면 이동에 실패
        process = False
        break
    fuel += to_arrival_fuel * 2  # 연료가 바닥나지 않을때 연료 충전


if process:  # 모든 승객 이동가능 할때
    print(fuel)
else:  # 아닐때
    print(-1)
