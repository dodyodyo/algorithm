from itertools import combinations

n = int(input())  # 보드의 크기 NxN
board = []  # 보드
teacher = []  # 선생의 좌표를 저장하는 리스트
blank = []  # 빈공간의 좌표를 저장하는 리스트

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teacher.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        elif board[i][j] == 'X':
            blank.append((i, j))


# 특정한 뱡향으로 감시를 진행(학생 발견 True, 학생 미발견 False)
def watch(x, y, direction):
    if direction == 0:
        while y < n:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            y += 1
    if direction == 1:
        while y >= 0:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            y -= 1
    if direction == 2:
        while x < n:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            x += 1
    if direction == 3:
        while x >= 0:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            x -= 1
    return False


# 장애물 설치 이후에
# 모든 선생에 대하여 동서남북 모두 감시되지 않는다면 피할 수 없음 False
# 어떤 선생에 대하여 동서남북중 어떤 곳에서 감시된다면 피할 수 있음 True
def avoid():
    for tx, ty in teacher:
        for i in range(4):
            if watch(tx, ty, i):
                return False
    return True


find = False
for object in combinations(blank, 3):  # 빈공간에서 3개를 꺼내 object에 3개의 좌표 저장
    for ox, oy in object:  # 보드에 장애물 설치
        board[ox][oy] = "O"
    # 어떤 선생에 대하여 동서남북중 어떤 곳에서 감시된다면
    if avoid():
        find = True
        break
    for ox, oy in object:  # 보드에 장애물 다시 없애기
        board[ox][oy] = "X"

if find:
    print("YES")
else:
    print("NO")
