import re

p = re.compile('(ABC)+')

m = p.search('ABCABCABC OK?')

print(m)
print(m.group())


p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")

m = p.search("park 010-1234-1234")


p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")

m = p.search("park 010-1234-1234")
print(m.group(1))


p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")

m = p.search("park 010-1234-1234")

print(m.group(2))


p = re.compile(r"(\w+)\s((\d+)[-]\d+[-]\d+)")

m = p.search("park 010-1234-1234")

print(m.group(3))


# 그루핑된 문자열 재참조하기
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())


# 그루핑된 문자열에 이름 붙이기
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")

m = p.search("park 010-1234-1234")

print(m.group("name"))

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')

print(p.search('Paris in the the spring').group())