f = open("C:/Users/user/Desktop/김재혁/Code/Jump To Python/Chapter 04/file/새파일.txt", 'w', encoding='utf-8')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)   # data를 파일 객체 f에 써라.
f.close()