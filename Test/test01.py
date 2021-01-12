# 1 거스름돈을 구하는 코드 작성
def solution1(price, money):
    answer = 0
    if sum(price) > money:
        answer = -1
    else:
        answer = money - sum(price)
    return answer

price = [2100, 3200, 2100, 800]
money = 10000
ret = solution1(price, money)
# print(f'solution1 함수의 반환 값은 {ret}입니다.')

# 2 총합에서 최댓값과 최솟값을 뺀 값을 구하는 코드 작성
def func_a(s): # 최댓값과 최솟값을 구하는 함수
    s.sort()
    return s[len(s)-1], s[0] # 한번에 return을 두개 할 수 있음

def func_b(s): # 총합을 구하는 함수
    ret = 0
    for i in s:
        ret += i
    return ret

def solution2(scores):
    sum = func_b(scores)
    max, min = func_a(scores)
    return sum - max - min

scores = [10,20,50,90,30,40]
ret = solution2(scores)
# print(f'solution2 함수의 반환 값은 {ret}입니다.')

# 3 학습 대상자 수를 구하는 코드 수정
def solution3(scores):
    count = 0
    for s in range(len(scores)): # scores를 len(scores)로 수정,
        # 아니라면 typeError 발생
        if scores[s] <= 200:
            count += 1
    return count

scores = [100, 200, 300, 400]
ret = solution3(scores)
# print(f'solution3 함수의 반환 값은 {ret}입니다.')

# 4 나라에 따른 관세를 구하는 코드 작성
def solution4(price, grade): # 할인인지 부과인지 주의
    answer = 0
    if grade == "S":
        answer = int(price * 1.05)
    elif grade == "G":
        answer = int(price * 1.1)
    elif grade == "V":
        answer = int(price * 1.15)
    return answer

price = 1300
grade = "G"
ret = solution4(price, grade)
# print(f'solution4 함수의 반환 값은 {ret}입니다.')

# 5 3,6,9 게임에서 박수를 몇 번 치는지 구하는 코드 빈칸채우기
def solution5(number):
    count = 0
    for i in range(1, number+1):
        current = i
        while current != 0:
            unit = current % 10 # 일의 자리수 구하기
            if unit == 3 or unit == 6 or unit == 9: # 3, 6, 9 판별
                count += 1 # 횟수 증가
            current //= 10 # 십의 자리수 구하기
    return count
number = 36
ret = solution5(number)
# print(f'solution5 함수의 반환 값은 {ret}입니다.')

# 6 교차점의 개수를 구하는 코드 빈칸 채우기 (만약에 나오면 패스..) ★★
def solution6(left_rings): # 쓰이지 않는 변수가 있는지 확인
    answer = 0
    for i in range(len(left_rings)):
        if left_rings[i] <= i: # 주로 index에 반복하는 변수가 들어감
            for k in range(i): # k의 반복문이기 때문에 문장에 k가 들어가야함
                if left_rings[k] > left_rings[i]:
                    answer += 1
    return answer

left_rings = [1, 4, 2, 5, 3]
ret = solution6(left_rings)
# print(f'solution6 함수의 반환 값은 {ret}입니다.')

# 7 파일 정보를 판별하는 코드 빈칸 채우기
def solution7(files_info):
    success = 0
    fail = 0
    for f in files_info:
        splited = f.split(".") # string.split('') 내장함수 중요
        # 안에 있는 문자로 문자열을 나누어 list로 반환
        # string to list
        if splited[0] == 'jpeg' and int(splited[-1]) < 1000:
            success += 1
        else:
            fail += 1
    return success, fail

files_info = ["jpeg.all.jpg.1500", "mpeg.all.mp3.500", "jpeg.all.jpg.800"]
success, fail = solution7(files_info)
# print(f'solution7 함수의 반환 값은 {success}, {fail}입니다.')

# 8 palindrome을 판별하는 코드 수정
def solution8(sentence):
    filtered = []
    for s in sentence:
        if s != ' ' and s != '.':
            filtered.append(s)
    before = ''.join(filtered) # ''.join(string) 내장함수 중요
    # ''안에 들어간 문자를 기준으로 합쳐서 string으로 반환
    # list to string
    filtered.reverse() # string.reverse() 역정렬하는 내장함수
    after = ''.join(filtered)
    return before == after

sentence = 'r   ace c.a.r'
ret = solution8(sentence)
# print(f'solution8 함수의 반환 값은 {ret}입니다.')

# 9 단어 안에서 중복되는 문자를 제거하는 함수 수정
def solution9(characters):
    result = [characters[0]] # 첫 문자를 초기화한 list를 넣음
    for i in range(1, len(characters)): # 1부터 끝까지
        if characters[i-1] != characters[i]: # 전 문자와 현재 문자를 비교
            result.append(characters[i]) # 같지 않으면 list에 추가 (새로운 list)
    return ''.join(result) # list to string 해서 반환

sentence = "seeennttteenccccceeee"
ret = solution9(sentence)
# print(f'solution9 함수의 반환 값은 {ret}입니다.')

# 10 특정 값보다 작은 값을 찾는 코드 수정
def solution10(data):
    total = 0
    for i in data: # data list 요소의 총 합을 구함
        total += i
    cnt = 0
    average = total // len(data)
    for i in data:
        if i < average: # <= 에서 < 으로 수정. 평균 미만인 조건 성립
            cnt += 1
    return cnt

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret = solution10(data)
print(f'solution10 함수의 반환 값은 {ret}입니다.')