# 튜플로 값을 묶는 행위를 가리켜 '튜플 패킹'이라 하고 반대로 튜플로 묶여 있는 값들을 풀어내느 행위를 '튜플 언패킹'이라 한다.

dice = [0, 1, 2, 3, 4, 5, 6]
# 튜플 언패킹 사용 x
temp = dice[6]
dice[6] = dice[3]
dice[3] = dice[1]
dice[1] = dice[4]
dice[4] = temp

# 튜플 언패킹 사용
dice[6], dice[3], dice[1], dice[4] = dice[3], dice[1], dice[4], dice[6]


a = 1
b = 3
# 튜플 언패킹 사용x
temp = a
a = b
b = temp
print(a, b)  # 3 1

# 튜플 언패킹 사용 o
a, b = b, a
print(a, b)  # 3 1
