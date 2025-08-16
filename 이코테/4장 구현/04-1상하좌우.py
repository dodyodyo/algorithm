# n을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()  # 문자열 공백으로 구분하여 입력받기

# L,R,U,D에 따른 이동 방향 차이값 dx,dy
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

# nx,ny: 이동 후 좌표
# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(nx, ny)
