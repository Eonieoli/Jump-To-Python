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

## 1. 정렬과 공백
print("%10s" % "hi")
print("%-10sjane" % "hi")

## 2.소수점 표현하기
print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)


# format 함수를 사용한 포매팅

## 1. 숫자 바로 대입하기
print("I eat {0} apples".format(3))

## 2. 문자열 바로 대입하기
print("I eat {0} apples".format("five"))

## 3. 숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples".format(number))

## 4. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. So I was sick for {1} days.".format(number, day))

## 5. 이름으로 넣기 (이름으로 넣으려면 format 함수에는 반드시 입력값이 있어야 한다.)
print("I ate {number} apples. So I was sick for {day} days.".format(number=10, day="three"))

## 6. 인덱스와 이름을 혼용해서 넣기 (format 함수에서 이름으로 입력값을 넣은 것은 순서로 계산하지 않기 때문에 {1}은 사용할 수 없다.)
print("I ate {0} apples. So I was sick for {day} days.".format(10, day="three"))

## 7. 왼쪽 정렬
print("{0:<10}".format("hi"))

## 8. 오른쪽 정렬
print("{0:>10}".format("hi"))

## 9. 가운데 정렬
print("{0:^10}".format("hi"))

## 10. 공백 채우기
print("{0:=^10}". format("hi"))
print("{0:!<10}".format("hi"))

## 11. 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

## 12. { 또는 } 문자 표현하기 (format 함수를 사용하면서 { 또는 } 문자를 표현하는 방법)
print("{{ and }}".format())
# print("{ and }")    # format 함수를 사용하지 않으면 그냥 쓰면 된다.

# f 문자열 포매팅
name = '홍길동'
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")
print(f"나는 내년이면 {age + 1}살이 된다.")
d = {'name': '홍길동', 'age': 30}
print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다.")

## 정렬
print(f"{"hi":<10}")    # 왼쪽 정렬
print(f"{"hi":>10}")    # 오른쪽 정렬
print(f"{"hi":^10}")    # 가운데 정렬

## 공백 채우기
print(f"{"hi":=^10}")   # 가운데 정렬하고 '='로 공백 채우기
print(f"{"hi":!<10}")   # 왼쪽 정렬하고 '!'로 공백 채우기

## 소수점 표현
y = 3.42134234
print(f"{y:0.4f}")      # 소수점 4자리까지만 표현
print(f"{y:10.4f}")     # 소수점 4자리까지 표현하고 총 자릿수를 '10'으로 맞춤
print(f"{y:^10.4f}")     # 소수점 4자리까지 표현하고 총 자릿수를 '10'으로 맞추고 가운데 정렬

## { 또는 } 문자 표현하기 (f 문자열에서 {}를 문자 그대로 표시하려면 2개를 동시에 사용해야 한다.)
print(f"{{ and }}")


# 1분 코딩
print("{0:!^12}".format("python"))
print(f"{"python":!^12}")