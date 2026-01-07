# 문자열 포매팅

## 1. 숫자 바로 대입
print("I eat %d apples." % 3)

## 2. 문자열 바로 대입
print("I eat %s apples." % "five")

## 3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)

## 4. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. So I was sick for %s days." % (number, day))