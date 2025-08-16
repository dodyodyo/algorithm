def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이 계산
    m = len(a[0])  # 열 길이 계산
    result = [[0] * n for _ in range(m)]  # 결과 리스트 열을 행으로 행을 열로
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


# 좌물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    length = len(new_lock) // 3
    for i in range(length, 2 * length):
        for j in range(length, 2 * length):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    M = len(key)
    N = len(lock)
    new_lock = [[0] * (3 * N) for _ in range(3 * N)]

    for i in range(N):
        for j in range(N):
            new_lock[N + i][N + j] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(2 * N):
            for y in range(2 * N):
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock) == True:
                    return True

                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 1, 1]]
print(solution(key, lock))
