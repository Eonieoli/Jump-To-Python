# 불 자료형의 값
## True: 참
## False: 거짓

a = True
b = False

print(type(a))
print(type(b))

print(1 == 1)
print(2 > 1)
print(2 < 1)

# 자료형의 참과 거짓
## 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면("", [], (), {}) 거짓이 되고, 비어 있지 않으면 참이 된다.
## 숫자에서는 그 값이 0일 때 거짓이 된다.
## None은 거짓을 뜻한다.

# 불 연산
print(bool('python'))
print(bool(""))
print(bool([1, 2, 3]))
print(bool([]))
print(bool((1, 2, 3)))
print(bool(()))
print(bool({'a': 1}))
print(bool({}))
print(bool(1))
print(bool(0))
print(bool(None))