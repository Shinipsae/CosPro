# p21
score = 75
if score > 80:
    print("81 이상일 때")
elif score > 60:
    print("61 부터 80 사이일 때")
elif score > 40:
    print("41부터 60 사이일 때")
elif score > 20:
    print("21부터 40 사이일 때")
else:
    print("20이하일 때")

# p27
li = [1, 2, 3, 4, 5]
print(li)
li.append(6)
print(li)
li.append([10, 20, 30])
print(li)

li = [1, 2, 3, 4, 5]
li.append(6)
print(li[5])
li.append([10, 20, 30])
print(li[6])
print(li[6][0])
# print(li[7])

# p28
first = [1, 2, 3]
second = [10, 20, 30]
first.append(second)
print(first)
# first, second은 서로 공유

first = [1, 2, 3]
second = first.copy()
print(first, "vs", second)
first[0] = 10
print(first, "vs", second)
# first, second은 서로 독립

string = "this is string constant"
char = 't'
char_count = 0
i = 0
while i < len(string):
    print(string[i], end='')
    if string[i] == char:
        char_count += 1
    i += 1
print("")
print(char + "'s count :" , char_count)

# p57
def func_a():
    num = 1
    global ga
    ga = 20
    print("func_a:", ga)

ga = 10
print('ga: ', ga)
func_a()
print()


