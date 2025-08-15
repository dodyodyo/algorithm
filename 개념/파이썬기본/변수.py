# """
# Global variable: 실행하는 파이썬 파일 전체 영역에서 사용 가능한 변수
# Local variable: 특정 지역 범위에서만 영향을 주고 받을 수 있는 변수'
# (ex: 특정 함수 내에서 선언한 변수는 return되지 않는 한 함수 밖에서 사용될 수 없다.)
# """

# a = 1  # Global


# def function():
#     print(a)
#     # 함수 내에서 별도 변수를 선언하지 않았으므로, Global과 구분되는 Local이 없음
#     # 함수 전체에 적용되는 Global 'a'가 적용됨


# function()  # 1 Global
# print(a)  # 1 Global


# """
# c와 c++과 달리 파이썬은 하나의 immutable값에 여러개의 참조가 붙는다.

# mutable: 변수가 선언되고 그 값을 바꿀 수 있는 경우
# 값을 바꿀 때 새로운 객체를 생성x (즉 값을 수정하더라도 주소 값이 바뀌지 않음)
# mutable객체의 경우 모든 객체를 각각 생성해서 참조
# list, dict


# immutable: 변수가 선언되고 그 값을 바꿀 수 없는 경우
# 값을 바꿀 때 새로운 객체를 생성 (즉 값을 수정하면 주소 값도 바뀜)
# immutable객체의 경우 값이 같은 경우에 변수에 상관없이 동일한 곳을 참조
# int, float, str, tuple
# 즉 mutable 객체의 값은 메모리에 각각 할당이 되고 immutable 객체의 값은, 동일한 값에 참조가 여러 개 붙는다

# """

# immutable 객체 (상태 변경 X)
print("immutable 객체")  # immutable 객체
# 0x7ffc9b414f68

# a,b,c,d,e의 주소가 모두 같은 곳을 가리킴
a = 99
b = 99
c = 99
d = 99
e = 99

print(hex(id(a)))  # 0x7ffc9b414f68
print(hex(id(b)))  # 0x7ffc9b414f68
print(hex(id(c)))  # 0x7ffc9b414f68
print(hex(id(d)))  # 0x7ffc9b414f68
print(hex(id(e)))  # 0x7ffc9b414f68


# mutable 객체 (상태 변경 O)
print("\nmutable 객체")  # mutable 객체
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
arr3 = [1, 2, 3]
arr4 = [1, 2, 3]

print(hex(id(arr1)))  # 0x21791664b40
print(hex(id(arr2)))  # 0x2179179b2c0
print(hex(id(arr3)))  # 0x2179180a300
print(hex(id(arr4)))  # 0x2179180a3c0


# immutable 객체
print("=" * 50)
print("immutable 객체 예제.")
print("=" * 50)

print("1. int 값이 변경되면?")
num1 = 99
num2 = 99
num3 = 99
num4 = 99

print(f"num1 값 : {num1} \t주소 : {hex(id(num1))}")
print(f"num2 값 : {num2} \t주소 : {hex(id(num2))}")
print(f"num3 값 : {num2} \t주소 : {hex(id(num3))}")
print(f"num4 값 : {num4} \t주소 : {hex(id(num4))}")

num1 += 1   # num1 값 증가
num3 += 1   # num3 값 증가
num4 += 10  # num4 값 증가

print(f"num1 값 : {num1} \t주소 : {hex(id(num1))}")
print(f"num2 값 : {num2} \t주소 : {hex(id(num2))}")
print(f"num3 값 : {num3} \t주소 : {hex(id(num3))}")
print(f"num4 값 : {num4} \t주소 : {hex(id(num4))}")

# mutable 객체
print("=" * 50)
print("mutable 객체 요소로 존재하는 immutable, mutable")
print("=" * 50)

arr1 = [55, 66, [11, 22], 'a', 'b']
arr2 = [55, 66, [11, 22], 'a', 'b']

# 리스트(immutable) 객체의 주소
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")


# 리스트 내부의 mutable 요소
# mutable
print()
print("-" * 50)
print('리스트 내부의 immutable 요소들')

print(f"arr1[0] : {arr1[0]} \t주소 : {hex(id(arr1[0]))}")
print(f"arr2[0] : {arr2[0]} \t주소 : {hex(id(arr2[0]))}")

print(f"arr1[1] : {arr1[1]} \t주소 : {hex(id(arr1[1]))}")
print(f"arr2[1] : {arr2[1]} \t주소 : {hex(id(arr2[1]))}")

print(f"arr1[3] : {arr1[3]} \t주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t주소 : {hex(id(arr2[3]))}")

print(f"arr1[4] : {arr1[4]} \t주소 : {hex(id(arr1[4]))}")
print(f"arr2[4] : {arr2[4]} \t주소 : {hex(id(arr2[4]))}")


# 리스트 내부의 mutable 요소
print()
print("-" * 50)
print('리스트 내부의 mutable 요소들')

print(f"arr1[2] : {arr1[2]} \t주소 : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]} \t주소 : {hex(id(arr2[2]))}")
