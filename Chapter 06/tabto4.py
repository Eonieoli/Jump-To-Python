import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src, 'r', encoding='utf-8')
tab_content = f.read()
f.close()

space_content = tab_content.replace('\t', ' ' * 4)

f = open(dst, 'w', encoding='utf-8')
f.write(space_content)
f.close()