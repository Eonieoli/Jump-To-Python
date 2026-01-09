# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result = sub(a = 7, b = 3)
print(result)

result = sub(b = 5, a = 3)
print(result)


# 입력값이 몇 개가 될지 모를 때

## 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

## 키워드 매개변수, kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)


# 함수의 리턴값은 언제나 하나이다
def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 4)      # 리턴값이 튜플로 변환돼서 result는 튜플이 된다.
print(result)

result1, result2 = add_and_mul(3, 4)
print(result1, result2)

# return을 만나면 함수를 빠져나간다
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)
say_nick('야호')
say_nick('바보')

# 매개변수에 초깃값 미리 설정하기
