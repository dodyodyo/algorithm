# 집합 자료형은 어떻게 만들까?
'''
iterable객체에 set()을 이용하여 만듦
iterable 객체가 아닌 iterable객체의 요소들이 개별적으로 들어감
hashable types(immutable 객체)만 가능 int, float, str, tuple (단, 튜플 안의 요소들도 해시 가능해야 함), frozenset 등 변경 불가능한 immutable 객체들
unhashable types(mutable 객체): list, dict, set, bytearray 
'''
# ------------------------------------------------------------------

# 리스트: 리스트 전체가 아니라 리스트 내부의 하나하나가 'set'으로 옮겨지면서 작동 따라서 list는 mutable 객체이므로 nonhashable하지만 list내의 요소는 immutable객체로 hashable하다
my_list = [1, 2, 3, 4]
my_set = set(my_list)  # {1, 2, 3, 4}

my_list = [1, 2, 3, 4]
my_set = set()
my_set.add(my_list)  # TypeError: unhashable type: 'list'

# 튜플
my_tuple = (1, 2, 3)
my_set = set(my_tuple)  # {1, 2, 3}

# 문자열
my_string = "Hello"
my_set = set(my_string)  # {'H', 'o', 'l', 'e'} # 중복 허용x, 순서x

# range
my_range = range(5)
my_set = set(my_range)  # {0, 1, 2, 3, 4}

# 다른 집합
another_set = {3, 4, 5}
my_set = set(another_set)  # {3, 4, 5}

# 만약 set()에 iterable이 아닌 객체를 전달한다면 오류
my_number = 123
my_set = set(my_number)  # TypeError: 'int' object is not iterable

# -----------------------------------------------------------------
# 집합 자료형의 특징
'''
중복을 허용하지 않는다.
순서가 없다.
리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 요솟값을 얻을 수 있지만, 집합과 딕셔너리는 순서가 없기때문에 인덱싱을 통해 요솟값을 얻을 수 없다. 
'''
# 인덱싱을 하려면 집합을 list()나 tuple()를 이용하여 리스트나 튜플 자료형으로 바꾸어 인덱싱한다.
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)  # [1, 2, 3]
print(l1[0])  # 1

t1 = tuple(s1)
print(t1)  # (1, 2, 3)
print(t1[0])  # 1

# -------------------------------------------------------------
# 교집합 합집합 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 구하기
print(s1 & s2)  # {4, 5, 6}
print(s1.intersection(s2))  # {4, 5, 6}

# 합집합 구하기
print(s1 | s2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합 구하기
print(s1 - s2)  # {1, 2, 3}
print(s2 - s1)  # {8, 9, 7}

print(s1.difference(s2))  # {1, 2, 3}
print(s2.difference(s1))  # {8, 9, 7}
# -------------------------------------------------------------------

# 집합 자료형 관련 함수
# 값 1개 추가하기 - add
# 이미 만들어진 set 자료형에 값을 추가할 수 있다. 1개의 값만 추가add할 때는 다음과 같이 하면 된다.
s1 = set([1, 2, 3])
s1.add(4)
print(s1)  # {1, 2, 3, 4}

# 값 여러 개 추가하기 - update
# 여러 개의 값을 한꺼번에 추가(update)할 때는 다음과 같이 하면 된다.
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)  # {1, 2, 3, 4, 5, 6}

# 특정 값 제거하기 - remove
# 특정 값을 제거하고 싶을 때는 다음과 같이 하면 된다.
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)  # {1, 3}
