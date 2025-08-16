# "균형잡힌 괄호 문자열"의 인덱스를 반환
# 균형잡힌 괄호 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리할 때 u는 더이상 분리되면 안되므로
# w의 왼쪽부터 보다가 균형잡힌 문자열이 만들어지면 u의 마지막 인덱스 반환
def balanced_index(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


# 올바른 괄호 문자열인지 반환
def check_proper(p):
    count = 0  # 왼쪽괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:  #  쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True  # 쌍이 맞는 경우에 True 반환


# 문자열 p가 "균형잡힌 괄호 문자열"일때
def solution(p):
    answer = ''
    if p == '':  #  입력이 빈 문자열 일때 빈 문자열을 반환
        return answer
    index = balanced_index(p)  # index에 u의 마지막 인덱스반환
    # p를 두 "균형잡힌 괄호 문자열" u,v로 반환
    u = p[: index + 1]
    v = p[index + 1 :]
    # u가 "올바른 괄호 문자열"이면, v에 대한 함수를 수행한 결과를 붙여봔환
    if check_proper(u):
        answer = u + solution(v)
    # u가 "올바른 괄호 문자열"이 아니라면, 아래의 과정을 수행
    else:
        answer = '('  # 빈 문자열에 첫 번재 문자로 '('를 붙인다.
        answer += solution(v)  # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
        answer += ')'
        u = list(u[1:-1])  # u의 첫 번째와 마지막 문자를 제거하고 리스트로 저장(why? 문자열은 값 변경 x)
        for i in range(len(u)):  # u의 모든 괄호 방향을 바꾼다.
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)  # 매개변수로 들어온 u리스트를 합쳐서 문자열로 반환
    return answer
