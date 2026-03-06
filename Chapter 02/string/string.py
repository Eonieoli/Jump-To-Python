# 문자열 만들기

## 1. 큰따옴표로 양쪽 둘러싸기
### "Hello World"

## 2. 작은따옴표로 양쪽 둘러싸기
### 'Python is fun'

## 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
### """Life is too short, You need python"""

## 4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
### '''Life is too short, You need python'''


# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때

# 1. 문자열에 작은따옴표 포함하기
food = "Python's favorite food is perl."
print(food)
# food = 'Python's favorite food is perl.'
# print(food)

# 2. 문자열에 큰따옴표 포함하기
say = '"Python is very easy." he says.'
print(say)
# say = ""Python is very easy." he says."
# print(say)

# 3. 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함하기
food = 'Python\'s favorite food is perl.'
say = "\"Python is very easy.\" he says."
print(food)
print(say)