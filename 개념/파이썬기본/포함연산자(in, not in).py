'''
in, not in  연산자는 데이터 안에 찾고자 하는 것이 있는지 없는지 확인하는 연사자이다.
in 연산자의 결과는 bool 타입이며 확인하고자 하는 데이터가 있는 경우 True, 없는 경우 False를 반환한다.
반대로 not in 연산자는확인하고자 하는 데이터가 있으면 False, 없으면 True를 반환한다.
'''

# --------------------------------------------------------
# 포함 연산자를 사용하는 사례
# 예시1 값이 있는지 확인 (리스트, 문자열, 튜플, 딕셔너리 등)
a = [1, 2, 3, 4, 5]

# if + True, False
if 1 in a:
    print("1 exist")  # 1 exist
else:
    print("1 not exist")

# True, False
print(2 in a)  # True


# 예시2 반복문에서 요소를 빼오는 데 사용
# for 반복문에서 in을 사용하는 것은 위에서 값이 있는지 확인하는 in과는 조금 다르다.
a = [1, 2, 3, 4, 5]

for val in a:
    print(val, end=' ')  # 1 2 3 4 5

'''
리스트 (list)
시간 복잡도: O(n)
이유: 리스트는 순차적으로 요소를 탐색하므로, 가장 최악의 경우 리스트의 끝까지 모든 요소를 확인해야 합니다. 리스트의 길이에 비례하여 시간이 걸립니다.

2. 튜플 (tuple)
시간 복잡도: O(n)
이유: 리스트와 마찬가지로 튜플도 순차적으로 요소를 탐색합니다. 따라서 탐색 시간은 튜플의 길이에 비례합니다.

3. 집합 (set)
시간 복잡도: O(1) 평균, O(n) 최악
이유: 집합은 해시 테이블로 구현되어 있어 평균적으로 O(1) 시간 복잡도로 요소를 탐색할 수 있습니다. 다만, 해시 충돌이 발생할 경우 최악의 경우 O(n)까지 걸릴 수 있습니다.

4. 딕셔너리 (dict)
시간 복잡도: O(1) 평균, O(n) 최악
이유: 딕셔너리도 해시 테이블을 사용하므로 키를 탐색하는 데 평균적으로 O(1) 시간이 소요됩니다. 해시 충돌이 발생하는 경우에는 O(n)까지 시간이 늘어날 수 있습니다.

5. 문자열 (str)
시간 복잡도: O(n)
이유: 문자열은 순차적으로 탐색하여 요소를 확인합니다. 문자열 길이에 비례하여 탐색 시간이 걸립니다.
'''


# --------------------------------------------------------------------
# 리스트에서의 활용
arr = ['a', 'b', 'c', 'd', 'e', 'f']

print(f"'a' in arr : {'a' in arr}")  # 'a' in arr : True
print(f"'a' not in arr : {'a' not in arr}")  # 'a' not in arr : False
print(f"'z' in arr : {'z' in arr}")  # 'z' in arr : False
print(f"'z' not in arr : {'z' not in arr}")  # 'z' not in arr : True

if 'c' in arr:
    print("c is in arr")  # c is in arr
else:
    print("c is not in arr")

# ---------------------------------------------------------------
# 딕셔너리에서의 활용
d = {'a': 123, 'b': 456, 'c': 789}

print(f"'a' in t : {'a' in d}")  # 'a' in t : True
print(f"'a' not in t : {'a' not in d}")  # 'a' not in t : False
print(f"'z' in t : {'z' in d}")  # 'z' in t : False
print(f"'z' not in t : {'z' not in d}")  # 'z' not in t : True

print(d.keys())  # dict_keys(['a', 'b', 'c'])
print(d.values())  #  dict_values([123, 456, 789])

# keys
if 'c' in d.keys():
    print("'c' in d.keys() : True")  # 'c' in d.keys() : True
else:
    print("'c' in d.keys() : False")

# values
if 456 in d.values():
    print("456 in d.values() : True")  # 456 in d.values() : True
else:
    print("456 in d.values() : False")

# ----------------------------------------------------------------------------
# 문자열에서의 활용
str = "BlockDMask"

# 전부 확인
if "BlockDMask" in str:
    print("'BlockDMask' in str : True")  # 'BlockDMask' in str : True
else:
    print("'BlockDMask' in str : False")

# 일부만 확인
if "Mask" in str:
    print("'Mask' in str : True")  # 'Mask' in str : True
else:
    print("'Mask' in str : False")


# 대소문자 구분 확인
if "mask" in str:
    print("'mask' in str : True")
else:
    print("'mask' in str : False")  # 'mask' in str : False


# 일부만 확인
if "z" not in str:
    print("'z' not in str : True")  # 'z' not in str : True
else:
    print("'z' not in str : False")

# 일부만 확인
if "k" not in str:
    print("'k' not in str : True")
else:
    print("'k' not in str : False")  # 'k' not in str : False
