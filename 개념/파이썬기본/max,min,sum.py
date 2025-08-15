"""
# max(), min()함수: 리스트 원소들을 순차적으로 비교하여 값을 반환

data = [[3, 2, 100], [3, 3, -1], [2, 0, 0]]
print(max(data))  # [3, 3, -1]
print(min(data))  # [2, 0, 0]
print(max(max(data)))  # 3
"""

"""
# 2차원 리스트에서 모든 원소의 최대/최솟값을 구할려면 map()함수가 필요
# map(): iterable을 받아서, 각 요소에 함수를 적용해주는 함수
min(map(min, data))
max(map(max, data))

data = [
    [6, 8, 2, 6, 2],
    [3, 2, 3, 4, 6],
    [6, 7, 3, 3, 2],
    [7, 2, 5, 3, 6],
    [8, 9, 5, 2, 7],
]

a = list(map(min, data))
b = list(map(max, data))
print(a)  # [2, 2, 2, 2, 2]
print(b)  # [8, 6, 7, 7, 9]
min_val = min(a)  # min(map(min, data))와 동일하다.
max_val = max(b)  # max(map(max, data))와 동일하다.
print(min_val)  # 2
print(max_val)  # 9
"""
#--------------------------------------------------------------------

# 이차원 리스트의 합을 구하는 방법
# 방법 1: for 루프를 사용한 합 구하기 
# 2차원 리스트 예시
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 합을 저장할 변수
total_sum = 0

# 각 행을 순회하며 요소를 더함
for row in matrix:
    for element in row:
        total_sum += element

print("Total Sum:", total_sum)  # 출력: 45

# 방법2: sum() 함수와 for 루프 사용하기
# 2차원 리스트 예시
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 각 행의 합을 더함
total_sum = sum(sum(row) for row in matrix)

print("Total Sum:", total_sum)  # 출력: 45
