# Key 리스트 만들기 - keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())         # dict_keys 객체를 반환한다. 반복문에서 사용할 수 있다.
print(list(a.keys()))   # 리스트로 만들고 싶으면 list(a.keys())로 써야 한다.

# Value 리스트 만들기 - values
print(a.values())       # dict_values 객체를 반환한다.

# Key, Value 쌍 얻기 - items
print(a.items())        # Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 반환한다.

# Key: Value 쌍 모두 지우기 - clear
a.clear()
print(a)

# Key로 Value 얻기 - get
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))

# dic[Key]와 dic.get(Key) 비교 (Key가 존재할 때는 동일하다.)
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('nokey'))       # Key가 없을 때, None 반환
# print(a['nokey'])           # Key가 없을 때, 오류 발생

## 딕셔너리 안에 찾으려는 Key가 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때는 get(x, '디폴트 값')을 사용하면 편리하다.
print(a.get('nokey', 'foo'))

# 해당 Key가 딕셔너리 안에 있는지 조사하기 - in
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print('name' in a)
print('email' in a)

# 1분 코딩
dic = {'name': '홍길동', 'birth': '1128', 'age': 30}
print(dic)