# 1부터 각 수까지의 합을 구하고, 그 차를 구하는 코드 작성
def func_a(k):
    sum = 0
    for i in range(1, k+1): # 1부터 수까지의 합
        sum += i
    return sum

def solution1(n, m):
    sum_to_m = func_a(m)
    sum_to_n = func_a(n)
    answer = sum_to_m - sum_to_n
    return answer

ret = solution1(5, 6)
# print(f"solution1 함수의 반환 값은 {ret}입니다.")

# 2 총합에서 최댓값과 최솟값을 뺀 값을 구하는 코드 작성
def func_a(s): # 최댓값을 구하는 함수
    ret = 0
    for i in s:
        if i > ret:
            ret = i
    return ret

def func_b(s):
    ret = 0
    for i in s: # 총합을 구하는 함수
        ret += i
    return ret

def func_c(s): # 최솟값을 구하는 함수
    ret = 101
    for i in s:
        if i < ret:
            ret = i
    return ret

def solution2(scores):
    sum = func_b(scores)
    max_score = func_a(scores)
    min_score = func_c(scores)
    return sum - max_score - min_score

scores = [50, 90, 65, 100]
ret = solution2(scores)
# print(f"solution2 함수의 반환 값은 {ret}입니다.")

# 3 가장 많은 방문객 수와 두번째로 많은 방문객 수의 차이를 구하는 코드 작성
def func_a(arr, n): # 가장 많은 방문객 수를 뺀 새로운 list를 만드는 함수
    ret = []
    for x in arr:
        if x != n:
            ret.append(x) # list 요소추가 -> append
    return ret

def func_b(a, b): # 두 수의 차이를 구하는 함수
    if a >= b:
        return a - b

def func_c(arr): # 가장 많은 방문객 수를 구하는 함수
    ret = -1
    for x in arr:
        if ret < x:
            ret = x
    return ret

def solution3(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor, max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first, max_second)
    return answer

visitor = [50, 20, 30, 10, 40]
ret = solution3(visitor)
# print(f"solution3 함수의 반환 값은 {ret}입니다.")

# 4 학점별 인원수를 구하는 코드 작성
def solution4(scores):
    grade_counter = [0 for i in range(5)] # 길이가 5인 list 0으로 초기화
    for x in scores:
        if x >= 85:
            grade_counter[0] += 1
        elif x >= 70:
            grade_counter[1] += 1
        elif x >= 55:
            grade_counter[2] += 1
        elif x >= 40:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter

scores = [50, 95, 70, 65, 90, 80, 60]
ret = solution4(scores)
# print(f"solution4 함수의 반환 값은 {ret}입니다.")

# 5 개구리가 점프한 횟수를 구하는 코드 작성
def solution5(stones):
    cnt = 0
    current = 0
    n = len(stones) # 돌의 개수
    while current < n: # 현재 개구리가 뛴 횟수가 돌의 개수보다 적을 때 까지
        current += stones[current] # 돌에 적혀있는 뛸 횟수를 누적함
        cnt += 1 # 횟수를 누적
    return cnt

stones = [2, 5, 1, 3, 2, 1]
ret = solution5(stones)
# print(f"solution5 함수의 반환 값은 {ret}입니다.")

# 6 키가 큰 사람의 수를 구하는 코드 수정
def solution6(height, k):
    answer = 0
    n = len(height)
    for h in height:
        if h > k: # >= 을 >로 수정, 이상이 아니라 초과조건
            answer += 1
    return answer

height = [165, 170, 175, 180, 184]
k = 175
ret = solution6(height, k)
# print(f"solution6 함수의 반환 값은 {ret}입니다.")

# 7 a는 z로, z는 a로 바꾸는 코드 수정
def solution7(s):
    s_list = list(s)
    n = len(s)
    for i in range(n):
        if s_list[i] == 'a':
            s_list[i] = 'z'
        elif s_list[i] == 'z': # if 를 elif로 수정, 중복 해당되지 않음
            s_list[i] = 'a'
    return ''.join(s_list)

name = 'james'
ret = solution7(name)
# print(f"solution7 함수의 반환 값은 {ret}입니다.")

# 8 이름의 특정 문자가 포함된 사람의 수를 구하는 코드 수정
def solution8(name_list):
    answer = 0
    for name in name_list:
        for n in name:
            if n =='j' or n == 'k':
                answer += 1
                break # continue를 break로 수정. 반환값을 return 해야함
    return answer

names = ['james', 'kim john', 'jonkin']
ret = solution8(names)
# print(f"solution8 함수의 반환 값은 {ret}입니다.")

# 9 거스름돈을 반환하는 코드 작성
def solution9(price, money):
    answer = 0
    sum = 0
    for p in price:
        sum += p # 내장함수인 sum()메소드도 사용 가능
    if sum > money:
        answer = -1
    else:
        answer = money - sum
    return answer

price = [2100, 3200, 2100, 800]
money = 10000
ret = solution9(price, money)
# print(f"solution9 함수의 반환 값은 {ret}입니다.")

# 10 k번째로 작은 수를 구하는 코드 작성
def solution10(array, k):
    new = []
    for arr in array: # 일차원 list에서 한번 거르기
        for a in arr: # 이차원 list에서 한번 더 거르기
            new.append(a) # 각 요소를 일차원 list에 담기
    new = sorted(new) # sorted(list_name) 내장함수
    return new[k-1]

arr = [[5, 12, 4, 31], [24, 13, 11, 2],
       [43, 44, 19, 26], [33, 65, 20, 21]]
k = 4
ret = solution10(arr, k)
print(f"solution10 함수의 반환 값은 {ret}입니다.")