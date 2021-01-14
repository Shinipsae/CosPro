def solution1(temperature, A, B):
    answer = 0
    for i in range(A+1, B):
        if temperature[i] > temperature[A] and temperature[i] > temperature[B]: answer += 1
    return answer
#아래는  테스트케이스  출력을  해보기  위한  코드입니다.
#아래에는  잘못된  부분이  없으니  위의  코드만  수정하세요.
temperature = [3, 2, 1, 5, 4, 3, 3, 2]
A = 1
B = 6
ret = solution1(temperature, A, B)
#[실행] 버튼을  누르면  출력  값을  볼  수  있습니다.
print("solution1 함수의  반환  값은", ret, "입니다.")

def solution2(papers, K):
    length = len(papers)
    for i, paper in enumerate(papers):
        K -= paper
        if K < 0:
            return i
    return length
#아래는  테스트케이스  출력을  해보기  위한  코드입니다. #아래에는  잘못된  부분이  없으니  위의  코드만  수정하세요.
papers1 = [2, 4, 2, 3, 1]
K1 = 10
ret1 = solution2(papers1, K1)
#[실행] 버튼을  누르면  출력  값을  볼  수  있습니다.
print("solution2 함수의  반환  값은", ret1, "입니다.")

#다음과  같이  import를  사용할  수  있습니다.
#import math
def solution3(people):
    answer = [0 for _ in range(4)]
    for p in people:
        if p < 95:
            answer[0] += 1
        elif p < 100:
            answer[1] += 1
        elif p < 105:
            answer[2] += 1
        elif p >= 105:
            answer[3] += 1
    return answer
#아래는  테스트케이스  출력을  해보기  위한  코드입니다.
people = [97, 102, 93, 100, 107]
ret = solution3(people)
#[실행] 버튼을  누르면  출력  값을  볼  수  있습니다.
print("solution3 함수의  반환  값은  ", ret, " 입니다.")

#다음과  같이  import를  사용할  수  있습니다.
#import math
def solution4(cards):
    #여기에  코드를  작성해주세요.
    answer = 0
    if cards[0][0] == cards[1][0] == cards[2][0]:
        answer = 3 * (int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1]))
    elif cards[0][0] == cards[1][0]:
        answer = 2 * (int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1]))
    elif cards[1][0] == cards[2][0]:
        answer = 2 * (int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1]))
    elif cards[1][0] == cards[2][0]:
        answer = 2 * (int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1]))
    else:
        answer = (int(cards[0][1]) + int(cards[1][1]) + int(cards[2][1]))
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution4(cards1)
#[실행] 버튼을  누르면  출력  값을  볼  수  있습니다.
print("solution4 함수의  반환  값은", ret1, "입니다.")

def solution5(money, price, n):
    answer = 0
    empty_bottle = answer = money // price
    while n <= empty_bottle:
        empty_bottle = empty_bottle + n
        answer += 1
        empty_bottle += 1
    return answer
#아래는  테스트케이스  출력을  해보기  위한  코드입니다. #아래에는  잘못된  부분이  없으니  위의  코드만  수정하세요.
money1 = 8
price1 = 2
n1 = 4
ret1 = solution5(money1, price1, n1)
#[실행] 버튼을  누르면  출력  값을  볼  수  있습니다.
print("solution5 함수의  반환  값은", ret1, "입니다.")

def solution6(password):
    capital_count, small_count, digit_count = 0, 0, 0
    for p in password:
        if p >= 'A' and p <= 'Z':
            capital_count += 1
        elif p >= 'a' and p <= 'z':
            small_count += 1
        elif p >= '0' and p <= '9':
            digit_count += 1
    if capital_count >= 1 and small_count >= 2 and digit_count >= 2:
        answer = True
    else:
        answer = False
    return answer
#아래는  테스트케이스  출력을  해보기  위한  코드입니다.
password1 = "helloworld"
ret1 = solution6(password1)
#[실행] 버튼을  누르면  출력  값을  볼  수  있습니다.
print("solution6 함수의  반환  값은", ret1, "입니다.")

def solution7(money, chairs, desks):
    answer = 0
    for chair in chairs:
        for desk in desks:
            price =  chair + desk
            if answer < price and answer < money : # price <= money
                answer = price
    return answer
#아래는  테스트케이스  출력을  해보기  위한  코드입니다.
money1 = 7
chairs1 = [2, 5]
desks1 = [4, 3, 5]
ret1 = solution7(money1, chairs1, desks1)
#[실행] 버튼을  누르면  출력  값을  볼  수  있습니다.
print("solution7 함수의  반환  값은", ret1, "입니다.")

def func_a(number1, number2):
    ret = 0
    if number1 > number2:
        ret = number1 - number2
    else:
        ret = number2 - number1
        return ret

def func_b(number):
    ret = 0

    while number != 0:
         number = number // 10
         ret += 1
    return ret

def func_c(number, digit):
    ret = 0

    for i in range(digit):
        temp = number % 10
        number = number // 10
        ret = ret * 10 + temp
    return ret

def solution8(number):
    answer = 0
    digit = func_b(number)
    convert_number = func_c(number, digit)
    answer = func_a(digit, convert_number)
    return answer
#아래는  테스트케이스  출력을  해보기  위한  코드입니다.
number1 = 120
ret1 = solution8(number1)
#[실행] 버튼을  누르면  출력  값을  볼  수  있습니다.
print("solution8 함수의  반환  값은", ret1, "입니다.")

def solution9(socks):
    answer = 0
    count = [0 for _ in range(10)]
    for s in socks:
        count[s] += 1
    for c in count:
        answer += (c // 2)
    return answer
#아래는  테스트케이스  출력을  해보기  위한  코드입니다. 아래에는 잘못된  부분이  없으니  위의  코드만  수정하세요.
socks = [1, 2, 1, 3, 2, 1]
ret = solution9(socks)
#[실행] 버튼을  누르면  출력  값을  볼  수  있습니다.
print("solution9 함수의  반환  값은", ret, "입니다.")

def solution10(weight, boxes):
    answer = 0
    for x in boxes:
        if x > int(weight * 1.1) or x < int(weight * 0.9):
            answer += 1
    return answer
#아래는  테스트케이스  출력을  해보기  위한  코드입니다.
weight = 600
boxes = [653, 670, 533, 540, 660]
ret = solution10(weight, boxes)
#[실행] 버튼을  누르면  출력  값을  볼  수  있습니다.
print("solution10 함수의  반환  값은", ret, "입니다.")


