# n,m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문할 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x좌표 ,y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸(0)이고 육지(0) 일때
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1  # 이동
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전한 이후 정면에 가본 칸(1) 이거나 바다(1) 일때
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈수 있다면(육지라면) 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:  # 뒤가 바다라면 끝내기
            break
        turn_time = 0

print(count)
