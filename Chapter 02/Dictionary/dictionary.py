# 딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고, Key를 통해 Value를 얻는다.
# {Key1: Value1, Key2: Value2, Key3: Value3, ...}

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

a = {1: 'hi'}           # Key로 정수, Value로 문자열을 사용한 예
a = {'a': [1, 2, 3]}    # Key로 문자열, Value로 리스트를 사용한 예


# 딕셔너리 쌍 추가, 삭제하기

## 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)

## 딕셔너리 쌍 삭제하기
del a[1]
print(a)


# 딕셔너리 사용하기

## 딕셔너리에서 Key를 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {1: 'a', 2: 'b'}
print(a[1])         # 1은 Key지, 인덱스가 아니다.
print(a[2])         # 2는 Key지, 인덱스가 아니다.

a = {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])


# 딕셔너리를 만들 때 주의할 사항

## 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다.
a = {1: 'a', 1: 'b'}
print(a)

## Key에 튜플(immutable)은 쓸 수 있지만 리스트(mutable)은 쓸 수 없다. Key는 변하지 않는(immutable) 값이어야 한다. 단, Value에는 변하는 값이든 변하지 않는 값이든 다 넣을 수 있다.
# a = {[1, 2]: 'hi'}      # 리스트를 Key로 사용했기 때문에, 오류 발생