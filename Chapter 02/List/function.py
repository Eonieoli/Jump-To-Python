# 리스트에 요소 추가하기 - append
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])    # 리스트 안에는 어떤 자료형도 추가할 수 있다.
print(a)

# 리스트 정렬 - sort
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']     # 문자는 알파벳 순서로 정렬한다. (오름차순 정렬 밖에 안 된다.)
a.sort()
print(a)

# 리스트 뒤집기 - reverse (정렬한 후에 뒤집는 게 아니라 현재의 리스트 요소 순서에서 뒤집는다.)
a = ['a', 'c', 'b']
a.reverse()
print(a)

# 인덱스 반환 - index
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
# print(a.index(0))   # a 리스트에 0이 존재하지 않으므로 에러 발생

# 리스트에 요소 삽입 - insert
a = [1, 2, 3]
a.insert(0, 4)      # a[0] 위치에 4 삽입
print(a)

a.insert(3, 5)
print(a)

# 리스트 요소 제거 - remove
a = [1, 2, 3, 1, 2, 3]
a.remove(3)     # a 리스트에서 첫 번째로 나오는 3을 삭제, 나머지 3은 그대로 존재한다.
print(a)

a.remove(3)
print(a)

# 리스트 요소 끄집어 내기 - pop
a = [1, 2, 3]
print(a.pop())      # pop()은 리스트의 마지막 요소를 반환하고 그 요소를 삭제한다.
print(a)

a = [1, 2, 3]
print(a.pop(1))     # pop(x)는 리스트의 x번째 요소를 반환하고 그 요소를 삭제한다.
print(a)

# 리스트에 포함된 요소 x의 개수 세기 - count
a = [1, 2, 3, 1]
print(a.count(1))   # count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 반환한다.

# 리스트 확장 - extend
a = [1, 2, 3]
a.extend([4, 5])    # extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다. a.extend([4, 5]) == a += [4, 5] == a = a + [4, 5]
print(a)
b = [6, 7]
a.extend(b)
print(a)