# 1
def solution1(cards):
    answer = 0
    for i in range(3):
        for k in range(i + 1, 5):
            for m in range(k + 1, 5):
                if (cards[i] + cards[k] + cards[m]) % 2 == 1:
                    answer += 1
    return answer

cards = [3, 5, 2, 7, 6]
ret = solution1(cards)
# print(f'solution1 함수의 반환 값'은 {ret}입니다.')

# 2
def func_a(arr):
    total = 0
    for i in arr:
        total += i
    return total

def solution2(arr, payload):
    answer = 0
    sum = func_a(arr)
    if sum >= payload:
        arr.sort()
        arr.reverse()
        weight = 0
        for i in range(len(arr)):
            diff = payload - weight
            if arr[i] <= diff:
                weight += arr[i]
                answer += 1
        if weight != payload:
            answer = 0
    return answer

arr = [2, 3, 5, 7, 13, 19, 23]
payload = 25
ret = solution2(arr, payload)
# print(f'solution2 함수의 반환 값은 {ret}입니다.')

# 3
def solution3(student):
    result = 0
    total = 0 # 학생 총 인원수
    for i in student:
        total += i
    result = total // 12
    if total % 12 != 0:
        result += 1
    return result
student = 50
ret = solution3(student)
print(f'solution3 함수의 반환 값은 {ret}입니다.')

# 4
def solution4(n, m):
    answer = 0
    OPEN, CLOSE = 0, 1
    room = [CLOSE for i in range(m+1)]
    for i in range(1, n+1):
        for k in range(1, m+1):
            if k % i == 0:
                room[k] = 1 - room[k]
    answer = room.count(OPEN)
    return answer
print(f'solution4 함수의 반환 값은 {ret}입니다.')

# 5
print(f'solution5 함수의 반환 값은 {ret}입니다.')

# 6
print(f'solution6 함수의 반환 값은 {ret}입니다.')

# 7
print(f'solution7 함수의 반환 값은 {ret}입니다.')

# 8
print(f'solution8 함수의 반환 값은 {ret}입니다.')

# 9
print(f'solution9 함수의 반환 값은 {ret}입니다.')

# 10
def solution10(positive, negative):
    answer = [0, 0]
    total = 0
    p_sum = 0
    n_sum = 0
    for i in range(4):
        for k in range(3):
            total += positive[i][k] + negative[i][k]
            p_sum += positive[i][k]
            n_sum += negative[i][k]
        answer[0] = int(p_sum / total * 100)
        answer[1] = int(n_sum / total * 100)
    return answer

positive = [
    [3, 2, 7],
    [4, 2, 6],
    [5, 3, 8],
    [7, 6, 8]
]
negative = [
[30, 50, 120],
[70, 90, 180],
[120, 150, 260],
[102, 120, 104]
]
ret = solution10(positive,negative)
print(f'solution10 함수의 반환 값은 {ret}입니다.')
