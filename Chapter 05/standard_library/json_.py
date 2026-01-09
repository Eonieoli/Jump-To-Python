import json

with open('myinfo.json', encoding='utf-8') as f:
    data = json.load(f)
print(type(data))
print(data)

data = {'name': '홍길동', 'birth': '0525', 'age': 30}
with open('myinfo.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

json_data = json.dumps(data)
print(json_data)

print(json.loads(json_data))

json_data = json.dumps(data, indent=2, ensure_ascii=False)
print(json_data)

print(json.dumps([1, 2, 3]))
print(json.dumps((4, 5, 6)))