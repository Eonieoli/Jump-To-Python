# 문자 개수 세기 - count
a = "hobby"
print(a.count('b'))

# 위치 알려주기 1 - find
a = "Python is the best choice"
print(a.find('b'))      # b가 처음 나온 위치 반환
print(a.find('k'))      # 찾는 문자나 문자열이 존재하지 않으면 -1 반환

# 위치 알려주기 2 - index
a = "Life is too short"
print(a.index('t'))       # t가 처음 나온 위치 반환
# print(a.index('k'))     # 찾는 문자나 문자열이 존재하지 않으면 오류 발생

# 문자열 삽입 - join
print(",".join('abcd'))                 # 문자열에 적용
print(",".join(['a', 'b', 'c', 'd']))   # 리스트나 튜플에도 적용 가능하다 => 반환되는 것은 문자열

# 소문자를 대문자로 바꾸기 - upper
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기 - lower
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기 - lstrip
a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기 - rstrip
a = " hi "
print(a.rstrip())

# 양쪽 공백 지우기 - strip
a = " hi "
print(a.strip())

# 문자열 바꾸기 - replace
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기 - split (반환은 리스트)
a = "Life is too short"
print(a.split())        # 공백을 기준으로 문자열 나눔
b = "a:b:c:d"
print(b.split(':'))     # :를 기준으로 문자열 나눔

##### 문자열 함수는 변경된 문자열을 반환하는 것이지, 해당 문자열 자체가 변경되는 것은 아니다. 문자열은 immutable하다.