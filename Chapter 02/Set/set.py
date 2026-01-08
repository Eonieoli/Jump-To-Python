# 집합
s1 = set([1, 2, 3])     # set() 괄호 안에 리스트를 입력하여 만들기
print(s1)

s2 = set("Hello")       # set() 괄호 안에 문자열을 입력하여 만들기
print(s2)

s3 = set()              # 비어 있는 집합 만들기
print(s3)

# set의 특징
## 중복을 허용하지 않는다.
## 순서가 없다.

## 인덱싱을 하고 싶으면, 리스트나 튜플로 변환해야 한다.
s1 = set([1, 2, 3])
l1 = list(s1)       # 리스트로 변환
print(l1)
print(l1[0])
t1 = tuple(s1)      # 튜플로 변환
print(t1)
print(t1[0])