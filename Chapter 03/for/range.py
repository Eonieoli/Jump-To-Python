# 0부터 10 전까지
a = range(10)
print(a)

# 1부터 11 전까지
a = range(1, 11)
print(a)

# 예시
add = 0
for i in range(1, 11):
    add = add + i

print(add)

# 1분 코딩
add = 0
for i in range(1, 101):
    add += i
print(add)

# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=' ')
    print('')