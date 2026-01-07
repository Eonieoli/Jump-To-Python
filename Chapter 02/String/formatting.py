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

### %s 포맷코드는 어떤 형태의 값이든 변환해서 넣을 수 있다.
print("I have %s apples." % 3)
print("rate is %s" % 3.234)
### 포맷코드를 쓰는 동시에 '%'문자 자체도 쓰고 싶으면 문자열 안에서 %%를 써야 한다.
# print("Error is %d%." % 98)
print("Error is %d%%." % 98)

# 포맷 코드와 숫자 함께 사용하기