# 1
print((80 + 75 + 55) / 3)

# 2
# 13을 2로 나눈 나머지가 0이면 짝수이고, 1이면 홀수이다.
print(13 % 2)   # 나머지가 1이므로 13은 홀수이다.

# 3
pin = "881120-1068234"
yymmdd = pin[:6]
num = pin[7:]
print(yymmdd)
print(num)

# 4
pin = "881120-1068234"
print(pin[7])

# 5
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# 6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 7
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

# 8
a = (1, 2, 3)
a = a + (4,)
print(a)

# 9
a = dict()
print(a)

a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'   # 딕셔너리의 Key는 immutable하기 때문에, 리스트는 딕셔너리의 Key가 될 수 없어서 오류 발생
a[250] = 'python'

# 10
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

# 11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# 12
a = b = [1, 2, 3]   # 이렇게 코딩하면 같은 리스트가 할당이 된다.
a[1] = 4
print(b)
print(a is b)

## 이때는 다른 리스트가 할당이 된다.
a, b = [1, 2, 3], [1, 2, 3]
print(a is b)