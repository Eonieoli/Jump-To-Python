# 문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
print(a[0:4])   # 0 <= a < 4
print(a[0:3])   # 0 <= a < 3

# 문자열을 슬라이싱하는 방법

## 공백 문자도 다른 문자와 동일하게 취급된다.
print(a[0:5])

## 꼭 앞이 0일 필요는 없다.
print(a[0:2])
print(a[5:7])
print(a[12:17])

## a[시작_번호:끝_번호]에서 끝_번호 부분을 생략하면 시작_번호부터 문자열의 끝까지 모두 출력
print(a[19:])

## a[시작_번호:끝_번호]에서 시작_번호 부분을 생략하면 문자열의 처음부터 끝_번호까지 모두 출력
print(a[:17])

## a[시작_번호:끝_번호]에서 시작_번호와 끝_번호를 모두 생략하면 문자열의 처음부터 끝까지 모두 출력
print(a[:])

## 슬라이싱에서도 - 기호를 사용할 수 있다.
print(a[19:-7])

## 슬라이싱으로 문자열 나누기
a = "20230331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = "20230331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)


# 문자열은 변경 불가능한(immutable) 자료형이어서 중간의 문자를 다른 문자로 수정할 수 없다.
# a = "Pithon"
# print(a[1])
# a[1] = 'y'
a = "Pithon"
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:])