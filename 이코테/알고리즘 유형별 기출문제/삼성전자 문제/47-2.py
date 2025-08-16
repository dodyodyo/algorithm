import copy

# 4 x 4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 방향 갑을 담는 테이블
array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[2 * j], data[2 * j + 1] - 1]

# 8가지 방향에 대한 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


# 현재 위치에서 왼쪽으로 회전한 결과 반화
def turn_left(direction):
    return (direction + 1) % 8


# 현재 배열에서 특정한 번호의 물고기 위치 찾기
# 그 번호의 물고기가 있으면 좌표 반환 없으면 없다는 None 반환
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None


# 모든 물괵를 회전 및 이동시키는 함수
# 배열과 현재 상어 위치 인수로 받음
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은 번호부터) 확인
    for i in range(1, 17):
        # 해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]  # 현재 물고기의 방향 정보 받음
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:  # 유효한 좌표
                    if not (nx == now_x and ny == now_y):  # 물고기의 위치가 상어의 위치가 아닐때
                        array[x][y][1] = direction  # 해당 물고기의 방향 회전
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]  # 물고기끼리 자리 바꿈
                        break
                direction = turn_left(direction)  # 물고기를 회전 시킴


# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]  # 현재 상어의 방향 정보
    # 현재의 방향으로 계속 이동시키기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 유효한 범위
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions


result = 0  # 최종 결과


# 모든 경우를 탐색하기 위한 DFS함수
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)  # 전달받는 array의 값을 바꾸지 않기 위해

    total += array[now_x][now_y][0]  # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1  #  물고기를 먹었으므로 번호 값을 -1로 변환

    move_all_fishes(array, now_x, now_y)  # 전체 물고기 이동시키기

    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total)
        return
    # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)


# 청소년 상어의 시작 위치(0,0)에서부터 재귀적으로 모든 경우 탐색
dfs(array, 0, 0, 0)
print(result)
