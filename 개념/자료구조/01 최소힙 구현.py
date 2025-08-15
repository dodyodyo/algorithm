# 부록A p455, 열혈c p342
# 힙: 1.완전 이진 트리 2.자식 노드의 우선순위 <= 부모노드의 우선순위
# 최대 힙: 루트 노드로 올라갈수록 저장된 값이 커지는 완전 이진 트리
# 최소 힙: 루트 노드로 올라갈수록 저장된 값이 작아지는 완전 이진 트리
# 파이썬은 최소 힙을 제공함
# 힙의 추가: 마지막 위치에 데이터를 두고서 부모노드와의 비교를 통해 자신의 위치를 찾아감
"""
힙의 삭제: 마지막 노드를 루트 노드의 자리로 옮긴 다음에, 자식 노드와의 비교를 통해서 제자리를 찾아감
두 개의 자식 노드 중 우선순위가 높은 자식과 부모노드를 교환해야 함
"""
import heapq


# iterable객체: 반복 가능한 객체(리스트, 사전 자료형, 튜플 자료형)
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
print(result)
