# 조건문: 참과 거짓을 판단하는 문장

## 비교 연산자(<. ?. ==, !=, >=, <=)
x = 3
y = 2
print(x > y)
print(x < y)
print(x != y)
print(x == y)

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

## 관계 연산자(and, or, not)
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

## 포함 연산자(in, not in)
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")


# 1분 코딩
if 'card' not in pocket:
    print("걸어가라")
else:
    print("버스를 타고 가라")


# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")