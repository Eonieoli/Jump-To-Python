f = open("./새파일.txt", 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()