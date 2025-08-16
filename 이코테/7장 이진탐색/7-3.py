# 이진 탐색 (반복문 이용)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 찾고자 하는 값이 중간점의 값보다 작은 경우
        elif array[mid] > target:
            end = mid - 1
        # 찾고자 하는 값이 중간점의 값보다 큰 경우
        else:
            start = mid + 1
    # 찾고자 하는 값이 존재하지 않으면 None 반환
    return None


# n(원소의 개수)와 target(찾고자 하는 정수)리스트로 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
