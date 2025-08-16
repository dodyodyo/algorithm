d = [0] * 101


def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 피보나치 결과 메모하고 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(100))
