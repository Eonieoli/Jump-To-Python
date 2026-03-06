import re

# sub
p = re.compile('(blue|white|red)')

print(p.sub('colour', 'blue socks and red shoes'))

print(p.sub('colour', 'blue socks and red shoes', count=1))


# subn
p = re.compile('(blue|white|red)')

print(p.subn('colour', 'blue socks and red shoes'))


# sub 메서드 사용 시 참조 구문 사용하기
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")

print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))


p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")

print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))


# sub 메서드의 매개변수로 함수 넣기

def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')

print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))