# # '''
# # 딕셔너리는 Key와 Value를 한 쌍으로 가지는 자료형이다. 예컨데 Key가 "baseball"이라면 Value는 "야구"가 될 것이다.
# # 딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다.
# # baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색하는 것이 아니라 baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다.
# # '''

# # # 딕셔너리의 기본 형태
# # # {Key1: Value1, Key2: Value2, Key3: Value3}
# # dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

# # # 딕셔너리 쌍 추가하기
# # a = {1: 'a'}
# # a[2] = 'b'
# # print(a)  # {1: 'a', 2: 'b'}

# # a['name'] = 'pey'
# # print(a)  # {1: 'a', 2: 'b', 'name': 'pey'}
# # a[3] = [1, 2, 3] # 인덱스가 아닌 key임에 중요!
# # print(a)  # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# # ------------------------------------------------------------------
# # 딕셔너리 요소 삭제하기
# # del 함수를 사용해서 del a[key]를 입력하면 지정한 Key에 해당하는 {Key: Value} 쌍이 삭제된다.
# a = {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
# del a[1]

# # ---------------------------------------------------------------
# # 딕셔너리 만들 때 주의할 사항
# # 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점에 주의해야 한다. 다음 예에서 볼 수 있듯이 동일한 Key가 2개 존재할 경우, 1: 'a' 쌍이 무시된다.
# a = {1: 'a', 1: 'b'}
# print(a)  # {1: 'b'}

# # Key에 리스트는 쓸 수 없다. 하지만 튜플은 Key로 쓸 수 있다.  Key는 immutable값만을 쓸 수 있다.
# a = {[1, 2]: 'hi'}
# '''
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
# '''

# --------------------------------------------------------------------
# 딕셔너리 관련 함수
# Key 리스트 만들기 -keys
# a.keys()는 딕셔너리 a의 Key만을 모아 dict_keys 객체를 리턴한다.
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# a.keys()는 딕셔너리 a의 Key만을 모아 dict_keys 객체를 리턴한다.
# 메모리 낭비를 줄이기 위해 dict_keys 객체를 리턴 리스트가 필요한 경우 list(a.key())를 사용하면 된다.
print(a.keys())  # dict_keys(['name', 'phone', 'birth'])
print(list(a.keys()))  # ['name', 'phone', 'birth']

# ---------------------------------------------------------------
# Value 리스트 만들기 - values
# values 함수를 호출하면 dict_values 객체를 리턴한다.
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.values())  # dict_values(['pey', '010-9999-1234', '1118'])
print(list(a.values()))  # ['pey', '010-9999-1234', '1118']
# --------------------------------------------------------------------

# Key, Value 쌍 얻기 - items
# items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴한다.
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.items())  # dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

# ------------------------------------------------------------
# Key: Value 쌍 모두 지우기 - clear
# clear 함수는 딕셔너리 안의 모든 요소를 삭제한다.
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.clear()
print(a)  # {}

# -------------------------------------------------------------
# Ke로 Value 얻기 - get
# a.get['name']은 a['name']과 같이 key 'name'에 해당하는 값을 얻음
# 존재하지 않는 키일때 a['nokey'] 방식은 오류를 발생시키고 a.get('nokey') 방식은 None을 리턴한다는 차이가 있다.
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))  # pey
print(a['name'])  # pey
print(a.get('nokey'))  # none
print(a['nokey'])  # 오류
