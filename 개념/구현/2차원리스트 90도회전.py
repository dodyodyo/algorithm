# a = [[1, 2, 3], [1, 2, 3]]
# print(len(a)) # 행 길이 계산 2
# print(len(a[0])) # 열 길이 계산3


# 이차원리스트를 시계 방향으로 90도 회전
def clockwise_90(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0] * n for _ in range(m)]  # 결과 리스트 열을 행으로 행을 열로
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


# 이차원리스트를 반시계 방향으로 90도 회전
def counterclockwise_90(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0] * n for _ in range(m)]  # 결과 리스트 열을 행으로 행을 열로
    for i in range(n):
        for j in range(m):
            result[m - 1 - j][i] = a[i][j]
    return result
