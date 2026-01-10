a = "Life is too short"
b = a.encode('utf-8')
print(b)
print(type(b))

a = "한글"
# a.encode("ascii")
print(a.encode('euc-kr'))
print(a.encode('utf-8'))