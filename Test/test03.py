# 1 두 사람의 거리 차이를 구하는 코드 작성
def solution1(a, b):
    answer = 0
    diff = a - b if a > b else b - a # 삼항연산자 ->
    # (참일때수행) if (조건) else (거짓일때수행)
    answer = 10 / diff
    return answer * 60 # 분으로 반환

a = 10
b = 8
ret = solution1(a, b)
# print(f'solution1 함수의 반환값은 {ret}입니다.')

# 2 예산을 배분하기 위한 금액을 구하는 코드 작성
def func_a(arr): # list 요소의 총 합을 구하는 함수
    total = 0
    for i in arr:
        total += i
    return total

def solution2(total, arr): # 총합을 받아 예산을 배분하는 함수
    result = []
    req_total = func_a(arr)
    for i in arr:
        if req_total > total:
            result.append(total // len(arr)) # 평균
        else:
            result.append(i)
    return result

total = 100
arr = [20, 20, 30, 40]
ret = solution2(total, arr)
# print(f'solution2 함수의 반환값은 {ret}입니다.')

# 3 가장 많이 같은 반을 보낸 학생을 찾는 코드 작성
def solution3(table):
    answer = 0
    max = 0
    for i in range(1, len(table)): # index 0은 선생님, i는 학생을 구분
        sum = 0
        for k in range(5): # 학년을 구분
            teacher = table[0][k]
            student = table[i][k]
            if teacher == student:
                sum += 1 # 학생 당 총합
        if max < sum: # 반복문 시행 후 총합 구함
            max = sum
            answer = i
    return answer

table = [
    [2, 6, 1, 7, 3],  # teacher
    [2, 9, 4, 6, 8],  # 1 student
    [6, 3, 4, 7, 1],  # 2
    [7, 7, 1, 1, 2],  # 3
    [8, 6, 9, 7, 3],  # 4
    [4, 6, 5, 9, 2]   # 5
   ]
ret = solution3(table)
# print(f'solution3 함수의 반환값은 {ret}입니다.')

# 4 페인트칠하는데 걸리는 시간을 구하는 코드 작성
def solution4(walls):
    answer = 0
    painted_walls = 0
    hour = 1
    while painted_walls < walls: # 벽을 다 칠하기 전까지
        painted_walls = hour + hour // 2 + hour // 4 # 정해져있음
        hour += 1 # 한번 실행시 마다 시간을 늘려줌
    answer = hour - 1 # 1로 초기화 했기 때문에 1을 빼줌
    return answer

walls = 5
ret = solution4(walls)
# print(f'solution4 함수의 반환값은 {ret}입니다.')

# 5 카드 게임의 승자를 알아내는 코드 작성
def solution5(mho_cards, mhe_cards):
    result = -1
    winner = [0] * 2 # 승자를 가리는 list 0으로 초기화
    for i in range(len(mho_cards)):
        if mho_cards[i] > mhe_cards[i]:
            winner[0] += 1 # 민호의 자리 winner[0]
        elif mhe_cards[i] > mho_cards[i]:
            winner[1] += 1 # 민희의 자리 winner[1]
    if winner[0] > winner[1]:
        result = 1
    elif winner[1] > winner[0]:
        result = 0
    return result # 무승부라면 처음 초기화했던 -1을 return

mho_cards = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11, 12, 13]
mhe_cards = [2, 1, 3, 4, 5, 9, 6, 7, 8, 10, 11, 12, 13]
ret = solution5(mho_cards, mhe_cards)
# print(f'solution5 함수의 반환값은 {ret}입니다.')

# 6 문자열 내 정수들의 총합을 구하는 코드 작성
def solution6(string):
    answer = 0
    number = 0
    s = string + ' ' # 숫자를 한번에 더하기 위해서 존재하는 공백
    for c in s:
        if c >= '0' and c <= '9': # c 가 정수이면
            number = number * 10 + int(c) # 한자리 씩 올리면서
            # 정수 변환
        else:
            answer += number
            number = 0
    return answer

string = "12korean34"
ret = solution6(string)
# print(f'solution6 함수의 반환값은 {ret}입니다.')

# 7 야구게임 판정하는 코드 작성
def solution7(a, b):
    result = [0, 0]
    for i in range(3):
        temp = b # 문제 숫자 넣기
        for k in range(3):
            if a % 10 == temp % 10: # 수가 같다면
                if i == k: # 자리도 같다면
                    result[0] += 1 # strike
                else:
                    result[1] += 1 # ball
            temp //= 10 # 다음 자릿수
        a //= 10 # b가 아니라 a의 자리를 줄임
    return result

a = 356
b = 356
ret = solution7(a, b)
# print(f'solution7 함수의 반환값은 {ret}입니다.')

# 8 문자열 내에 지정하는 문자들이 있는지 확인하는 코드 작성
def solution8(password, key):
    answer = 0
    match_cnt = 0
    for k in key: # key를 먼저
        for p in password:
            if k == p: # 같으면
                match_cnt += 1 # 1 증가
                break
    if match_cnt >= len(key): # 적어도 key 자릿수보다 같거나 커야 함.
        answer = 1
    return answer

password = "1234lsa korean uk"
key = "klu"
ret = solution8(password, key)
# print(f'solution8 함수의 반환값은 {ret}입니다.')

# 9
def solution9(scores):
    result = [0, 0, 0, 0]
    for i in range(4):
        for k in range(4):
            if i != k:
                result[i] += scores[i][k] * 2
    return result

scores = [[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]]
ret = solution9(scores)
# print(f'solution9 함수의 반환값은 {ret}입니다.')

# 10
def solution10(strings):
    result = 0
    for s in strings:
        length = len(s)
        result += (length // 4)
        if length % 4 != 0:
            result += 1
    return result

strings = ["1234", "1234", "1234"]
ret = solution10(strings)
print(f'solution10 함수의 반환값은 {ret}입니다.')
