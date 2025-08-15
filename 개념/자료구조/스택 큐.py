"""
스택
파이썬에서 스택은 리스트를 이용해서 구현
stack = []

top: 삽입과 삭제가 일어나는 위치
s.append(data): top위치에 현재 있는 데이터를 삭제하고 학인하는 연산
s.pop(): top위치에 있는 데이터를 삭제하고 확인하는 연산
s[-1]: sPeek, top위치에 있는 데이터를 삭제하지 않고 확인하는 연산
"""

"""
큐
파이썬에서 큐는 deque를 이용하여 구현
from collections import deque 
q = deque()

front, rear
q.append(data): rear부분에 새로운 데이터를 삽입하는 연산
q.popleft(): front부분에 있는 데이터를 삭제하고 확인하는 연산
q[0]: 큐의 맨 앞(front)에 있는 데이터를 확인할 때 사용하는 연산
"""
