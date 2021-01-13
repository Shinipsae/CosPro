# 1 축구장 임대료를 구하는 코드 작성
def solution1(n, price):
    games = n * (n-1) // 2 # 총 경기 수
    per_day = n // 2 # 하루에 진행될 경기 수
    answer = (games // per_day) * price
    return answer

teams = 7
price = 100000
ret = solution1(teams, price)
# print(f'solution1 함수의 반환값은 {ret}입니다.')

# 2 축구화 주문 수량을 구하는 코드 작성
def solution2(shoes_size):
    answer = [0] * 6
    for s in shoes_size:
        if s == '7':
            answer[0] += 1
        elif s == '7.5':
            answer[1] += 1
        elif s == '8':
            answer[2] += 1
        elif s == '8.5':
            answer[3] += 1
        elif s == '9':
            answer[4] += 1
        elif s == '9.5':
            answer[5] += 1
    return answer

shoes_size = ['7','7.5','8','8.5','9','9.5']
ret = solution2(shoes_size)
# print(f'solution2 함수의 반환값은 {ret}입니다.')

# 3 방문객 수의 차이를 구하는 코드 작성
def func_a(arr, num): # 최댓값을 뺀 새로운 list를 구하는 함수
    ret = []
    for i in arr:
        if i != num:
            ret.append(i)
    return ret

def func_b(a, b): # 최댓값과 그 다음 큰 값의 차이를 구하는 함수
    if a > b:
        return a - b
    else:
        return b - a

def func_c(arr): # list에서 최댓값을 구하는 함수
    ret = -1
    for i in arr:
        if ret < i:
            ret = i
    return ret

def solution3(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor, max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first, max_second)
    return answer

visitor = [1, 3, 2, 4, 5, 3, 6, 3, 7, 4, 5, 7]
ret = solution3(visitor)
# print(f'solution3 함수의 반환값은 {ret}입니다.')

# 4 학점 별 인원수를 구하는 코드 작성
def solution4(scores):
    grade_counter = [0 for i in range(5)]
    for i in scores:
        if i >= 85:
            grade_counter[0] += 1
        elif i >= 70:
            grade_counter[1] += 1
        elif i >= 55:
            grade_counter[2] += 1
        elif i >= 40:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter

scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ret = solution4(scores)
# print(f'solution4 함수의 반환값은 {ret}입니다.')

# 5 빈도를 구하는 코드 작성
def func_a(arr): # 회원당 쓴 글의 개수를 할당하는 함수
    counter = [0 for _ in range(1001)]
    for i in arr:
        counter[i] += 1
    return counter

def func_b(arr): # 쓴 글중 빈도의 최댓값을 구하는 함수
    ret = 0
    for i in arr:
        if ret < i:
            ret = i
    return ret

def func_c(arr): # 쓴 글중 빈도의 최솟값을 구하는 함수
    ret = func_b(arr)
    for i in arr:
        if i != 0 and ret > i:
            ret = i
    return ret

def solution5(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

arr = [1, 2, 3, 1, 1, 2, 1, 2, 1, 2, 3, 1, 1, 1, 1, 1]
ret = solution5(arr)
# print(f'solution5 함수의 반환값은 {ret}입니다.')

# 6 몸무게가 큰 사람의 수를 구하는 코드 작성
def solution6(weight, k):
    answer = 0
    for w in weight:
        if w > k:
            answer += 1
    return answer

weights = [65, 70, 75, 80, 84]
ret = solution6(weights, 75)
# print(f'solution6 함수의 반환값은 {ret}입니다.')

# 7 문자열 내 숫자를 변환하는 함수 수정 (더해서 9가 되어야 함)
def solution7(s):
    answer = []
    for c in s:
        if '0' <= c <= '9': # 한번에 표현 가능
            n = ord('i') - ord(c) # ord -> char to ASCII code
            c = chr(n) # chr -> ASCII code to ord
        answer.append(c)
    return ''.join(answer)

s = 'ab1c3d'
ret = solution7(s)
# print(f'solution7 함수의 반환값은 {ret}입니다.')

# 8 이름에 특정 문자가 포함된 개수를 구하는 코드 작성
def solution8(name_list):
    answer = 0
    for name in name_list:
        for char in name:
            # string.find('') 문자가 있으면 index, 없으면 -1 반환
            if char.find('A') > -1 or char.find('K') > -1:
            # if 'A' in char or 'K' in char: 도 가능
                answer += 1
                break
    return answer

names = ['Adios', "Kickboard Association", "google"]
ret = solution8(names)
# print(f'solution8 함수의 반환값은 {ret}입니다.')

# 9 제품 포장을 위한 포장상자의 개수를 구하는 코드 작성
def solution9(orders): # 문제 버려....
    answer = 0
    size = 0
    for o in orders:
        for i in range(6):
            if o[i] != 0:
                size += ((i+1)**2) * o[i]
    if answer % 36 != 0:
        answer += 1
    return answer

orders = [[0, 0, 4, 0, 1 ,1], [7, 5, 1, 0, 1, 0]]
ret = solution9(orders)
# print(f'solution9 함수의 반환값은 {ret}입니다.')

# 10 ISBN 규칙을 확인하는 코드 작성
def sum_isbn(isbn):
    sum = 0
    for i in range(len(isbn)):
        c = int(isbn[i])
        if i % 2: # 홀수 index이면 3을 곱함
            w = 3
        else: # 0이나 짝수 index이면 1을 곱함
            w = 1
        sum += w * c # 곱한 값을 누적
    return sum

def solution10(isbn):
    answer = ''
    answer = str(10 - (sum_isbn(isbn[:12]) % 10))
    if answer == '10':
        answer = 0
    return answer # 숫자를 반환

isbn = '9788970508122'
ret = solution10(isbn)
print(ret == '2')
print(f'solution10 함수의 반환값은 {ret}입니다.')