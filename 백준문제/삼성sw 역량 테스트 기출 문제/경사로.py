n, l = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = 0

for i in range(n):
    runway = [[0] * n for _ in range(n)]
    for j in range(n - 1):
        if board[i][j] < board[i][j + 1]:
            runway[i][j] += 1
            