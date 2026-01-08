# for 문 사용
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)

# 리스트 컴프리헨션
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# 리스트 컴프리헨션 안에 if 문
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# 중첩된 리스트 컴프리헨션
result = [x*y for x in range(2, 10)
          for y in range(1, 10)]
print(result)