# 문자열 비교하기

# 완전 일치
"ABC" == "ABC"  # True
"ABC" == "abc"  # False
"ABC" != "ABC"  # False
"ABC" != "abc"  # True

# 부분 일치
print("Feat." in "에잇(Prod.&Feat. SUGA of BTS)")  # True
print("Feat." not in "에잇(Prod.&Feat. SUGA of BTS)")  # False

# 전방 일치
# 문자열이 해당 피텅으로 시작하는지에는 startswith가 사용
# 패텅을 여러 개 지정할 경우 이들과 하나라도 전방 일치 한다면 Tue를 반환함

phonenumber = "010-1234-5678"
phonenumber.startswith("010")  # True

phonenumber = "010-1234-5678"
phonenumber.startswith("011")  # False

phonenumber = "010-1234-5678"
phonenumber.startswith(("010", "011"))  # True

# 후방 일치
# 문자열이 해당 피텅으로 끝나는지 endswith가 사용
# 패텅을 여러 개 지정할 경우 이들과 하나라도 후방 일치 한다면 Tue를 반환함

name = "김대한 씨"
print(name.endswith("씨"))  # True

name = "김대한 씨"
name.endswith("님")  # False

name = "김대한 씨"
name.endswith(("씨", "님"))  # True
