import re

# 전방 탐색의 필요성
p = re.compile(".+:")

m = p.search("http://google.com")

print(m.group())


# 긍정형 전방탐색
p = re.compile(".+(?=:)")

m = p.search("http://google.com")

print(m.group())


# 부정형 전방 탐색
p = re.compile(".*[.](?!bat$).*$")