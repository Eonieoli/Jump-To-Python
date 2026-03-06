import re

p = re.compile('\section')
print(p.findall('\section \\section \\\section \\\\section'))

p = re.compile('\\section')
print(p.findall('\section \\section \\\section \\\\section'))

p = re.compile('\\\\section')
print(p.findall('\section \\section \\\section \\\\section'))

p = re.compile(r'\section')
print(p.findall('\section \\section \\\section \\\\section'))

p = re.compile(r'\\section')
print(p.findall('\section \\section \\\section \\\\section'))