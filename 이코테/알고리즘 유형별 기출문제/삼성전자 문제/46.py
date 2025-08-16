from collections import deque

INF = int(1e9)  # 무한

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_distance():
    distance = [[-1] * n for i in range(n)]
    distance[nowx][nowy] = 0
    q = deque([(nowx, nowy)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 자신의 크기보다 작거나 같은 경우에 지나갈 수 있음
                if distance[nx][ny] == -1 and data[nx][ny] <= now_size:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
    return distance


n = int(input())


data = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 9:
            nowx, nowy = i, j  # 현재 상어 위치
            data[nowx][nowy] = 0  # 자기 자신을 먹으면 안되니 0으로 초기화

now_size = 2  # 현재 사이즈
time = 0  # 시간
ate = 0  # 먹은 횟수

while True:
    distance = find_distance()
    min = INF

    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일때
            if distance[i][j] != -1 and 1 <= data[i][j] < now_size:
                # 가장 가까운 물고기 1마리만 선택(거리가 같으면 가장 왼쪽 위 선택)
                if distance[i][j] < min:
                    nextx, nexty = i, j
                    min = distance[i][j]

    if min == INF:  # 먹을 수 있는 물고기가 업는 경우
        print(time)
        break
        
    else:  # 먹을 수 있는 물고기가 있는 경우
        nowx, nowy = nextx, nexty  # 현재 좌표 옮기고
        data[nowx][nowy] = 0  # 물고기 삭제

        time += min
        ate += 1
        # 자신의 크기만큼 먹었을때 현재 크기 증가
        if ate == now_size:
            now_size += 1
            ate = 0
