max_product_number = 10

def func_a(gloves):
    counter = [0 for _ in range(max_product_number + 1)]
    for x in gloves:
        counter[x] += 1
    return counter


def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)

    total = 0
    for i in range(1, max_product_number + 1):
        total += min(left_counter[i], right_counter[i])
    return total


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
left_gloves = [2, 1, 2, 2, 4]
right_gloves = [1, 2, 2, 4, 4, 7]
ret = solution(left_gloves, right_gloves)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

###########################################################

def func_a(arr):
    count = 0
    for n in arr:
        if n % 5 == 0:
            count += 1
    return count

def func_b(three, five):
    if three > five:
        return "three"
    elif three < five:
        return "five"
    else:
        return "same"

def func_c(arr):
    count = 0
    for n in arr:
        if n % 3 == 0:
            count += 1
    return count

def solution(arr):
    count_three = func_c(arr)
    count_five = func_a(arr)
    answer = func_b(count_three, count_five)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [2, 3, 6, 9, 12, 15, 10, 20, 22, 25]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

###########################################################

def solution(schedule):
    answer = []
    for idx, i in enumerate(schedule):
        if i == 'X':
            answer.append(idx + 1)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"]
ret = solution(schedule)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#enumerate() : (index, 컬렉션원소) 의 튜플 형태로 반환

###########################################################

#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(words):
    #여기에 코드를 작성해주세요.
    answer = ''
    for word in words:
        if len(word) >= 5:
            answer += word
        else:
            pass
    if answer == '':
        answer = 'empty'
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1);

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2);

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")

###########################################################

def func_a(bundle, start):
    return bundle[start::2]

def func_b(score1, score2):
    if score1 > score2:
        return [1, score1]
    elif score2 > score1:
        return [2, score2]
    else:
        return [0, score1]

def func_c(bundle):
    answer = 0
    score_per_cards = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    for card in bundle:
        answer += score_per_cards[card]
    return answer

def solution(n, bundle):
    a_cards = func_a(bundle, 0)[:n]
    b_cards = func_a(bundle, 1)[:n]
    a_score = func_c(a_cards)
    b_score = func_c(b_cards)
    return func_b(a_score, b_score)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

###########################################################

def solution(floors):
    dist = 0
    length = len(floors)
    for i in range(1, length):
        if floors[i] > floors[i-1]:
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1] - floors[i]
    return dist

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
floors = [1, 2, 5, 4, 2]
ret = solution(floors)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

###########################################################

def solution(value, unit):
    converted = 0
    if unit == "C":
        value = value * 1.8 + 32
    if unit == "F":
        value = (value - 32) / 1.8
    converted = int(value)
    return converted

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
value = 527
unit = "C"
ret = solution(value, unit)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

###########################################################

def solution(number):
    count = 0
    while number > 0:
        n = number % 10
        if n == 2 or n == 3 or n == 5 or n == 7:
            count += 1
        number //= 10
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
number = 29022531
ret = solution(number)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

###########################################################

def solution(votes, N, K):
    counter = [0 for _ in range(N + 1)]
    for x in votes:
        counter[x] += 1
    answer = 0
    for c in counter:
        if c == K:
            answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]
N = 5
K = 2
ret = solution(votes, N, K)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

###########################################################

def solution(purchase):
    total = 0
    for p in purchase:
        if p >= 1000000:
            total += 50000
        elif p >= 600000:
            total += 30000
        elif p >= 400000:
            total += 20000
        elif p >= 200000:
            total += 10000
    return total

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
purchase = [150000, 210000, 399990, 990000, 1000000]
ret = solution(purchase)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")





