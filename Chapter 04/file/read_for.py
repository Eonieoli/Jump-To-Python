f = open("./새파일.txt", 'r', encoding='utf-8')
for line in f:
    print(line)
f.close()