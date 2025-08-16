from collections import deque

# 재귀함수로 구현
def left(num, dir):
    if num <= 0:
        return
    if gear[num - 1][2] != gear[num][6]:
        left(num - 1, -dir)
        gear[num - 1].rotate(-dir)


def right(num, dir):
    if num >= 3:
        return
    if gear[num][2] != gear[num + 1][6]:
        right(num + 1, -dir)
        gear[num + 1].rotate(-dir)


gear = []
for i in range(4):
    gear.append(deque(list(map(int, input()))))

k = int(input())

for _ in range(k):
    num, dir = map(int, input().split())
    num -= 1

    # 왼쪽과 오른쪽 먼저 처리한 후 중앙 톱니바퀴 회전
    left(num, dir)
    right(num, dir)
    gear[num].rotate(dir)

result = gear[0][0] + 2 * gear[1][0] + 4 * gear[2][0] + 8 * gear[3][0]
print(result)
