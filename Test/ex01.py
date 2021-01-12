# 1. 셔츠 사이즈를 담은 list를 반환하는 코드 작성
def solution1(shirt_size):
    answer = [0] * 6 # 크기가 6인 list 0으로 초기화
    for size in shirt_size: # java for-each
        if size == "XS":
            answer[0] += 1 # 각 자리에 1씩 증가
        elif size == "S":
            answer[1] += 1
        elif size == "M":
            answer[2] += 1
        elif size == "L":
            answer[3] += 1
        elif size == "XL":
            answer[4] += 1
        elif size == "XXL":
            answer[5] += 1
    return answer # 정답 list return

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution1(shirt_size)
print(f"solution1 함수의 변환값은 {ret}입니다.")

# 2 회원등급에 따른 할인율로 판매가를 계산하는 코드 작성
def solution2(price, grade):
    answer = 0
    if grade == "S": # 5% 할인 -> 95% 가격으로 판매
        answer = int(price * 0.95)
    elif grade == "G":
        answer = int(price * 0.9)
    elif grade == "V":
        answer = int(price * 0.85)
    return answer

price1 = 2500
grade1 = "V"
ret1 = solution2(price1, grade1)
print(f"solution2 함수의 반환 값은 {ret1} 입니다.")

price2 = 96900
grade2 = "S"
ret2 = solution2(price2, grade2)
print(f"solution2 함수의 반환 값은 {ret2} 입니다.")

# 3 두 날짜의 차를 계산하는 코드 작성
def func_a(month, day): # 1월 1일부터 현재 날짜까지의 일수를 계산
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(0, month-1):
        total += month_list[i]
    total += day
    return total - 1

# 두 날짜사이의 일수 차를 계산
def solution3(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

start_month = 1
start_day = 31
end_month = 2
end_day = 2
ret = solution3(start_month, start_day, end_month, end_day)
print(f'solution3 함수의 반환 값은 {ret} 입니다.')

# 4 list에서 가장 많은 수와 적은 수 개수의 배수차이를 구하는 코드 작성
def func_a(arr): # 길이가 1000인 list를 0으로 초기화
    counter = [0 for _ in range(1001)]
    for x in arr: # list의 해당 숫자 index에 1씩 증가
        counter[x] += 1
    return counter

def func_b(arr): # list에서 최댓값을 구하는 함수
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr): # list에서 0초과의 최솟값을 구하는 함수
    ret = 1001
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution4(arr): # 최종 답을 구하는 함수
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution4(arr)
print(f'solution4 함수의 반환 값은 {ret} 입니다.')

# 5 list를 역정렬하는 코드 작성
def solution5(arr): 
    left, right = 0, len(arr)-1
    while right > left: # 오른쪽의 index가 오른쪽보다 클 때까지
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 4, 2, 3]
ret = solution5(arr)
print(f'solution5 함수의 반환 값은 {ret} 입니다.')

# 6 369 게임에서 박수를 몇 번 치는지 구하는 코드 작성
def solution6(number): 
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0: # 0이 아닐때 까지
            # 일의 자리가 3,6,9 인지 판별
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                count += 1 # 박수
                print("짝", end='')
            current = current // 10 # 한 자리를 줄임
        if temp == count:
            print(i, end='')
        print('', end='')
    print('')
    return count

number = 20
ret = solution6(number)
print(f'solution6 함수의 반환 값은 {ret}입니다.')

# 7 범위에 맞는 토익점수를 판별하는 코드 작성
def solution7(scores):
    count = 0
    for s in scores:
        if 650 <= s and s < 800: # 두 조건을 모두 만족해야함
            count += 1
    return count

scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution7(scores)
print(f'solution7 함수의 반환 값은 {ret}입니다.')

# 8 palindrome 단어인지 판별하는 코드 작성
def solution8(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ': # .과 공백이 모두 아니어야함
            str += c
    size = len(str)
    for i in range(size // 2): # 반까지만 검사해도 됨
        if str[i] != str[size-1-i]:
            return False
    return True

sentence1 = "racecar."
ret1 = solution8(sentence1)
print(f'solution8 함수의 반환 값은 {ret1}입니다.')

sentence2 = "never odd or even."
ret2 = solution8(sentence2)
print(f'solution8 함수의 반환 값은 {ret2}입니다.')

# 9 한 단어 안에서 중복되는 알파벳을 없애는 코드 작성
def solution9(characters):
    result = ''
    result += characters[0] # 첫 번째 글자는 초기화
    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]: # 전 알파벳과 현재 알파벳이 같은지 검사
            result += characters[i]
    return result

characters = 'senteeeencccccceeee'
ret = solution9(characters)
print(f'solution9 함수의 반환 값은 {ret}입니다.')

# 10 list 요소의 평균보다 작은 요소가 몇 개인지 구하는 코드 작성
def solution10(data):
    total = sum(data)
    average = total / len(data) 
    cnt = 0
    for d in data:
        if d <= average: # 평균보다 작으면 
            cnt += 1 # cnt 증가시킴
    return cnt

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 5.5
ret1 = solution10(data1)
print(f'solution10 함수의 반환값은 {ret1}입니다.')

data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10] # 1.9
ret2 = solution10(data2)
print(f'solution10 함수의 반환값은 {ret2}입니다.')