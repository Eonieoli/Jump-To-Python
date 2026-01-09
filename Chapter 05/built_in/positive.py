def positive(l):
    result = []                 # 양수만 걸러내서 저장할 변수
    for i in l:
        if i > 0:
            result.append(i)    # 리스트에 i 추가
    return result

print(positive([1, -3, 2, 0, -5, 6]))