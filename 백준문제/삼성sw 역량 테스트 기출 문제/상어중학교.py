from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

INF = -9


# 일반 블록의 좌표를 인수로 받아 블록 그룹을 찾고 크기, 무지개 블록의 수, 기준 블록의 행, 열을 반환하는 함수
def find_block(x, y):
    num = board[x][y]  # 블록그룹의 일반블록 숫자
    size, rainbow_cnt = 0, 0
    rx, ry = x, y
    visited = [[False] * n for _ in range(n)]

    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        size += 1
        if board[x][y] == 0:
            rainbow_cnt += 1
        if 1 <= board[x][y] <= m:
            if x < rx or (x == rx and y < ry):
                rx, ry = x, y

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and (board[nx][ny] == num or board[nx][ny] == 0):
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return size, rainbow_cnt, rx, ry


# 일반 블록의 좌표를 받아 블록 그룹의 모든 블록을 제거한다.
def remove(x, y):
    num = board[x][y]
    visited = [[False] * n for _ in range(n)]

    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        board[x][y] = INF
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and (board[nx][ny] == num or board[nx][ny] == 0):
                    q.append((nx, ny))
                    visited[nx][ny] = True


def gravitation():
    for y in range(n):
        for x in range(n - 2, -1, -1):  # 가장 아래 행은 검사할 필요 없음
            if 0 <= board[x][y] <= m:  # 검은색 블록을 제외한 모든 블록
                nx = x
                while nx + 1 < n and board[nx + 1][y] == INF:  # 다음 위치가 유효하고 INF인 경우에만
                    nx += 1
                if nx != x:  # 블록이 이동한 경우에만 갱신
                    board[nx][y] = board[x][y]  # 블록을 아래로 이동
                    board[x][y] = INF  # 원래 위치를 INF로 설정


def counterclockwise_90(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0] * n for _ in range(m)]  # 결과 리스트 열을 행으로 행을 열로
    for i in range(n):
        for j in range(m):
            result[m - 1 - j][i] = a[i][j]
    return result


n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = 0
while True:
    # 블록 그룹 찾기
    max_size, max_rainbow_cnt, max_rx, max_ry = -1, -1, -1, -1
    for i in range(n):
        for j in range(n):
            if 1 <= board[i][j] <= m:  # 일반 블록일때
                size, rainbow_cnt, rx, ry = find_block(i, j)  # 사이즈, 무지개수, 기준x, 기준y
                if (size > max_size) or (size == max_size and rainbow_cnt > max_rainbow_cnt) or (size == max_size and rainbow_cnt == max_rainbow_cnt and rx > max_rx) or (size == max_size and rainbow_cnt == max_rainbow_cnt and rx == max_rx and ry > max_ry):
                    max_size = size
                    max_rainbow_cnt = rainbow_cnt
                    max_rx = rx
                    max_ry = ry
                    bx, by = i, j
    if max_size < 2:
        print(result)
        break

    remove(bx, by)  # 블록 그룹의 모든 블록을 제거
    result += max_size**2  # 블록의 수의 제곱점 획득
    gravitation()  # 격자에 중력이 작용한다.
    board = counterclockwise_90(board)  # 격자가 90도 반시계 방향으로 회전한다.
    gravitation()  # 다시 격자에 중력이 작용한다.
