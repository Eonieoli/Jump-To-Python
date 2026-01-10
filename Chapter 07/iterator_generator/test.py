a = [1, 2, 3]
# print(next(a))

ia = iter(a)
print(type(ia))
print(next(ia))
print(next(ia))
print(next(ia))
# print(next(ia))     # StopIteration

a = [1, 2, 3]
ia = iter(a)
for i in ia:
    print(i)

# 이터레이터는 for 문을 이용하여 반복하고 난 후에는 다시 반복하더라도 더는 그 값을 가져오지 못한다.
# 즉, for 문이나 next로 그 값을 한 번 읽으면 그 값을 다시는 읽을 수 없다는 특징이 있다.
for i in ia:
    print(i)            # 값이 출력되지 않는다.

def mygen():
    yield 'a'
    yield 'b'
    yield 'c'

g = mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))      # StopIteration