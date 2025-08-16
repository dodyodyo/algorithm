dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
score = [0, 1, 10, 100, 1000]


def satisfy():
    result = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            for i in range(n**2):
                if board[x][y] == likeSet[i][0]:
                    st = i
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in likeSet[st][1:]:
                        cnt += 1
            result += score[cnt]
    return result


def position(like):
    max_like = -1
    max_blank = -1
    px, py = -1, -1  # 초기화
    for x in range(n):
        for y in range(n):
            if board[x][y] == -1:
                like_cnt, blank_cnt = 0, 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in like:
                            like_cnt += 1
                        if board[nx][ny] == -1:
                            blank_cnt += 1
                if like_cnt > max_like or (like_cnt == max_like and blank_cnt > max_blank):
                    max_like = like_cnt
                    max_blank = blank_cnt
                    px, py = x, y
    return px, py


board = [[-1] * n for _ in range(n)]
likeSet = []
for _ in range(n**2):
    likeSet.append(list(map(int, input().split())))

for i in range(n**2):
    x, y = position(likeSet[i][1:])
    board[x][y] = likeSet[i][0]

print(satisfy())


# ------------------------------------------
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
score = [0, 1, 10, 100, 1000]


def satisfy():
    result = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            for i in range(n**2):
                if board[x][y] == likeSet[i][0]:
                    st = i
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in likeSet[st][1:]:
                        cnt += 1
            result += score[cnt]
    return result


def position(like):
    max_like = -1
    max_blank = -1
    px, py = -1, -1  # 초기화
    for x in range(n):
        for y in range(n):
            if board[x][y] == -1:
                like_cnt, blank_cnt = 0, 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in like:
                            like_cnt += 1
                        if board[nx][ny] == -1:
                            blank_cnt += 1
                if like_cnt > max_like:
                    max_like = like_cnt
                    max_blank = blank_cnt
                    px, py = x, y
                elif like_cnt == max_like:
                    if blank_cnt > max_blank:
                        max_blank = blank_cnt
                        px, py = x, y
    return px, py


board = [[-1] * n for _ in range(n)]
likeSet = []
for _ in range(n**2):
    likeSet.append(list(map(int, input().split())))

for i in range(n**2):
    x, y = position(likeSet[i][1:])
    board[x][y] = likeSet[i][0]

print(satisfy())
