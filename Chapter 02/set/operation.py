s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 구하기
print(s1 & s2)
print(s1.intersection(s2))
print(s2.intersection(s1))

# 합집합 구하기
print(s1 | s2)
print(s1.union(s2))
print(s2.union(s1))

# 차집합 구하기
print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))