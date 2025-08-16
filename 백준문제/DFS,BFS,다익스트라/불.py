from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    dist = [[-1] * w for _ in range(h)]  # 이동 거리 저장하는 2차원 배열

    sx, sy = sangeun[0]  # 상근의 위치 입력받음
    if sx == 0 or sx == h - 1 or sy == 0 or sy == w - 1:
        print(1)  # 초기 위치가 가장자리면 바로 탈출 가능
        return

    sq = deque(sangeun)
    fq = deque(fire)
    dist[sx][sy] = 0
    while sq:  # 상근이 탈출할 때까지
        f_cnt = len(fq)  # 각 턴에 정해진 개수만큼 불이 이동
        for _ in range(f_cnt):
            x, y = fq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.':  # 유효한 범위이면서 빈공간일때
                    board[nx][ny] = '*'  # 불 번짐
                    fq.append((nx, ny))  # 큐에 저장

        s_cnt = len(sq)  # # 각 턴에 정해진 개수만큼 상근이 이동
        for _ in range(s_cnt):
            x, y = sq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.':  # 유효한 범위에서 빈공간일 때
                    board[nx][ny] = '@'
                    sq.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    if nx == 0 or nx == h - 1 or ny == 0 or ny == w - 1:  # 빠져나올수 있다면 즉시 종료
                        print(dist[nx][ny] + 1)
                        return
    print("IMPOSSIBLE") # 반복문을 그냥 빠져나온다면 탈출할 수 없는 것임


t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    w, h = map(int, input().split())  # 열과 행
    fire = []
    sangeun = []
    board = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire.append((i, j))
            if board[i][j] == '@':
                sangeun.append((i, j))
    bfs()
