# 1
def solution1(shirt_size):
    answer = [0] * 6
    for size in shirt_size:
        if size == "XS":
            answer[0] += 1
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
    return answer

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution1(shirt_size)
# print(f"solution 함수의 변환값은 {ret}입니다.")

# 2
def solution2(price, grade):
    answer = 0
    if grade == "S":
        answer = int(price * 0.95)
    elif grade == "G":
        answer = int(price * 0.9)
    elif grade == "V":
        answer = int(price * 0.85)
    return answer

price1 = 2500
grade1 = "V"
ret1 = solution2(price1, grade1)
# print(f"solution 함수의 반환 값은 {ret1} 입니다.")

price2 = 96900
grade2 = "S"
ret2 = solution2(price2, grade2)
# print(f"solution 함수의 반환 값은 {ret2} 입니다.")

# 3
def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(0, month-1):
        total += month_list[i]
    total += day
    return total - 1

def solution3(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

start_month = 1
start_day = 31
end_month = 2
end_day = 2
ret = solution3(start_month, start_day, end_month, end_day)
# print(f'solution 함수의 반환 값은 {ret} 입니다.')

# 4
def func_a(arr):
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr):
    ret = 1001
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution4(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution4(arr)
# print(f'solution 함수의 반환 값은 {ret} 입니다.')

# 5
def solution5(arr):
    left, right = 0, len(arr)-1
    while right > left:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 4, 2, 3]
ret = solution5(arr)
# print(f'solution 함수의 반환 값은 {ret} 입니다.')

# 6
def solution6(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        temp = count
        while current != 0:
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                count += 1
            #   print("짝", end='')
            current = current // 10
#       if temp == count:
#           print(i, end='')
#       print('', end='')
#   print('')
    return count

number = 20
ret = solution6(number)
# print(f'solution 함수의 반환 값은 {ret}입니다.')

# 7
def solution7(scores):
    count = 0
    for s in scores:
        if 650 <= s and s < 800:
            count += 1
    return count

scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution7(scores)
# print(f'solution 함수의 반환 값은 {ret}입니다.')

# 8
def solution8(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size-1-i]:
            return False
    return True

sentence1 = "racecar."
ret1 = solution8(sentence1)
# print(f'solution 함수의 반환 값은 {ret1}입니다.')

sentence2 = "never odd or even."
ret2 = solution8(sentence2)
# print(f'solution 함수의 반환 값은 {ret2}입니다.')

# 9
def solution9(characters):
    result = ''
    result += characters[0]
    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]:
            result += characters[i]
    return result

characters = 'senteeeencccccceeee'
ret = solution9(characters)
# print(f'solution 함수의 반환 값은 {ret}입니다.')

# 10
def solution10(data):
    total = sum(data)
    average = total / len(data)
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret1 = solution10(data1)
print(f'solution 함수의 반환값은 {ret1}입니다.')

data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ret2 = solution10(data2)
print(f'solution 함수의 반환값은 {ret2}입니다.')