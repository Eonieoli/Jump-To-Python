# 함수의 구조
def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)

# 매개변수와 인수

# 입력값과 리턴값에 따른 함수의 형태

## 일반적인 함수
a = add(3, 4)
print(a)

## 입력값이 없는 함수
def say():
    return "Hi"

a = say()
print(a)

## 리턴값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))
add(3, 4)
a = add(3, 4)
print(a)

## 입력값도 리턴값도 없는 함수
def say2():
    print("Hi")

say2()