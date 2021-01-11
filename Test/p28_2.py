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