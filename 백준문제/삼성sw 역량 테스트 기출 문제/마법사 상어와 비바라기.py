dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

mx = [-1, 1, 1, -1]
my = [1, 1, -1, -1]


def move():
    # 방향에 맞게 구름 이동
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + dx[dir] * s) % n
        cloud[i][1] = (cloud[i][1] + dy[dir] * s) % n


def rain():
    for i in range(len(cloud)):
        board[cloud[i][0]][cloud[i][1]] += 1


def magic():
    for i in range(len(cloud)):
        x, y = cloud[i][0], cloud[i][1]
        cnt = 0
        for j in range(4):
            nx = x + mx[j]
            ny = y + my[j]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                cnt += 1
        board[cloud[i][0]][cloud[i][1]] += cnt


def make_cloud():
    global cloud  # 재할당시 지역변수가 되므로 전역변수로 계속사용하기 위해 global이 필요
    new_cloud = []
    # 현재 구름 좌표를 set으로 만들어 탐색 시간 최적화
    current_cloud_set = set((x, y) for x, y in cloud)  # 집합 자료형은 hashable(immutable)만 가능
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i, j) not in current_cloud_set:
                new_cloud.append([i, j])
                board[i][j] -= 2
    cloud = new_cloud


def sum_water():
    return sum(sum(row) for row in board)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cloud = [[n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]]
for _ in range(m):
    dir, s = map(int, input().split())
    move()
    rain()
    magic()
    make_cloud()
print(sum_water())
