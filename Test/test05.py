# 1
def solution1(arr):
    answer = 0
    energy = 40
    for i in arr:
        if energy < i:
            energy = 40
            answer += i
        energy -= i # 남아있는 기름 양
    return answer

arr = [20, 10, 30, 30, 20, 10]
ret = solution1(arr)
print(ret)

# 2
def solution2(arr):
    answer = 0
    price = 0
    for i in range(len(arr)):
        price = arr[i]
        if (i+1) % 4 == 0:
            price -= int(arr[i] * 0.5)
            # price //= 2
        answer += price
    return answer

arr = [100, 500, 200, 400, 300]
ret = solution2(arr)
print(ret)

# 3
def func_a(a, length):
    for i in range(len(a)):
        if a[i] >= length:
            return i
    return -1

def solution3(N, orders):
    material = [8 for _ in range(N)]
    k = 0
    price = 0
    for o in orders:
        k = func_a(material, o)
        if k >= 0:
            material[k] -= o
            price += 3000 * o
    return price

# 실행
orders = [1,3,5,7,8]
ret = solution3(10, orders)
print(ret)

# 4
def solution4(word):
    num2alpha = ["oqz","ij","abc","def","gh","kl","mn","prs","tuv","wxy"]
    answer = ' '
    for c in word:
        for i in range(len(num2alpha)):
            for a in num2alpha[i]:
                if a == c:
                    answer += str(i)
                    break
    return answer

# 실행
word = 'whitepawn'  # 941837296
ret = solution4(word)
print(ret)

# 5
def func_a(a):
    return ((a // 100) * 60) + (a % 100)

def solution5(arr):
    answer = 0
    min_a = func_a(2200)
    for i in arr:
        min_b = func_a(i)
        elapsed_minute = min_a - min_b
        answer += 1000 + (elapsed_minute // 10) * 500
    return answer

# 실행
arr = [2100,2015]
ret = solution5(arr)
print(ret)

# 6
def solution6(down, up):
    answer = 0
    passenger = 0
    n = len(down)
    for i in range(n):
        passenger += up[i] - down[i]
        stand = passenger - 240
        if stand < 0:
            stand = 0
        if stand > 0 and stand > answer:
            answer = stand
    return answer

# 실행
up = [240, 100, 0, 160, 10, 140]
down = [0, 0, 140, 80, 0, 0]
ret = solution6(down, up)
print(ret)

# 7
def solution7(price):
    sales = [0 for _ in range(len(price))]
    j = 0
    for i in price:
        if i[0] < 5000:
            percent = 0.25
        elif i[0] < 15000:
            percent = 0.20
        elif i[0] < 100000:
            percent = 0.15
        else:
            percent = 0.1
        sales[j] = i[0] * percent * i[1]
        j += 1
    return func_a(sales)

def func_a(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    return min

# 실행
price = [
    [50000, 10],
    [15000, 20],
    [5000, 40],
    [150000, 100]
]
ret = solution7(price)
print(ret)

# 9
def solution(answer):
    min = 1
    max = 100
    result = 0
    for i in answer:
        result = (max + min) // 2
        if min == max or i == 'c':
            break
        if i == 'u':
            max = int(result)
        if i == 'd':
            min = int(result)
    return result

answer = 'uddc'    # 테스트 값
ret = solution(answer)
print(ret)

# 10
def solution(wats, bill):
    result = [0 for _ in range(8)]
    unit_price = int(bill / wats[0]) + 1
    for i in range(8):
        result[i] = wats[i+1] * unit_price
    return result

# 실행(테스트)
bill = 200000
wats = [3600, 10, 20, 30, 40, 50, 60, 70, 80]
ret = solution(wats, bill)
print(ret)



