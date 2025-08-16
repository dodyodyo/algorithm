n, m, k = map(int, input().split())  # 격자크기, 상어의 개수, 냄새 지속 시간

array = []  # 현재 상어의 위치를 저장하는 2차원 리스트
for _ in range(n):
    array.append(list(map(int, input().split())))

# 현재 상어의 방향 정보
directions = list(map(int, input().split()))

# 각 위치마다 [특정 냄새의 상어정보, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 방향 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# 위, 아래, 왼쪽, 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 모든 냄새 정보를 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j][0] = 0
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]


# 모든 상어를 이동
def move():
    # 이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_array = [[0] * n for _ in range(n)]
    # 각 위치를 하났씩 확인하며
    for x in range(n):
        for y in range(n):
            if array[x][y] != 0:  # 상어가 존재하는 경우
                direction = directions[array[x][y] - 1]  # 그 상어의 이동방향 저장
                found = False
                # 우선순위상 다음 어떤 곳에서 냄새가 없을 때
                for index in range(4):
                    # 우선순위상 다음 곳
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx < n and 0 <= ny < n:  # 유효한 범위
                        if smell[nx][ny][1] == 0:  # 냄새가 존재하지 않을때
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]  # 현재 상어의 방향 수정하기
                            if new_array[nx][ny] == 0:  # 상어끼리 만나지 않을 때
                                new_array[nx][ny] = array[x][y]
                            else:  # 상어끼리 만난다면
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])  # 낮은번호의 상어가 살아남음
                            found = True
                            break
                if found:
                    continue

                # 우선순위상 다음 모든 곳에서 냄새가 없을때
                for index in range(4):
                    # 우선순위상 다음 곳
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx < n and 0 <= ny < n:  # 유효한 범위
                        if smell[nx][ny][0] == array[x][y]:  # 자신의 냄새가 있는 곳일때
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]  # 현재 상어의 방향 수정하기
                            new_array[nx][ny] = array[x][y]  # 상어 이동시키기
                            break
    return new_array


time = 0
while True:
    update_smell()  # 모든 위치의 냄새를 업데이트
    array = move()  # 모든 상어를 이동시키기
    time += 1  # 시간 증가

    # 1번 상어만 남았는지 확인
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False

    if check:  # 1번 상어만 남았다면
        print(time)
        break

    if time >= 1000:  # 1000초가 지날 때까지 끝나지 않았다면
        print(-1)
        break
