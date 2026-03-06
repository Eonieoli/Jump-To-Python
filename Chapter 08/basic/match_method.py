import re

p = re.compile('[a-z]+')

# match
m = p.match("python")

print(m.group())

print(m.start())

print(m.end())

print(m.span())


# search
m = p.search("3 python")

print(m.group())

print(m.start())

print(m.end())

print(m.span())