from copy import copy

# 변수: 객체를 가리키는 것

a = 1
b = "python"
c = [1, 2, 3]

a = [1, 2, 3]
print(id(a))


# 리스트를 복사하고자 할 때
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)

a[1] = 4
print(a)
print(b)

## 1. [:] 이용하기
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

## 2. copy 모듈 이용하기
a = [1, 2, 3]
b = copy(a)     # b = a[:]와 동일하다. 또는 b = a.copy() 파이썬 내장 함수 copy() 사용
print(b is a)


# 변수를 만드는 여러 가지 방법

## 여러 개의 변수를 한 번에 할당하기
a, b = ('python', 'life')
print(a, b)
(a, b) = 'python', 'life'
print(a, b)
a, b = 'python', 'life'
print(a, b)
[a, b] = ['python', 'life']
print(a, b)
[a, b] = 'python', 'life'
print(a, b)

## 여러 개의 변수에 같은 값을 대입하기
a = b = 'python'
print(a, b)

### 값 바꾸기
a = 3
b = 5
a, b = b, a
print(a, b)


# 1분 코딩
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)