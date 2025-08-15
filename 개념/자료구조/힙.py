"""
우선순위큐: 우선순위가 가장 높은 데이터를 가장 먼저 삭제 한다.
우선순위큐를 구현하는 방법: 배열, 연결리스트, 힙

heapq라이브러리, PriorityQueue라이브러리 이용
보통 heapq이 더 빠르므로 heapq를 사용


파이썬의 힙은 최소 힙으로 구성되어 있으므로
단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
최소 힙 자료구조의 최상단 원소는 항상 '가장 작은 원소'이다

< heapq 라이브러리 >
import heapq
h = []
heapq.heappush(h): 힙에 원소를 삽입한다. 파이썬에서 튜플(a,b)로 힙에 입력하면 첫번째 원소를 기준으로 정렬한다.
heapq.heappop(h, value): 힙에서 원소를 꺼낸다.

< PriorityQueue >
from queue imoprt PriorityQueue 
que = PriorityQueue()
que = PriorityQueue(maxsize = 8) # 큐의 최대 크기 8
que.put(value)
que.get()





"""

# 최소 힙 구현
import heapq


def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 최대 힙 구현
# 파이썬에서는 최대 힙을 제공하지 않음
# 힙에 원소를 삽입하기 전에 잠시 부호를 바꾸었다가
# 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.

import heapq


def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 부호를 바꾸어 차례대로 힙이 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 부호르 바꾸어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
