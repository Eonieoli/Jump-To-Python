import re

# |
p = re.compile('Crow|Servo')

m = p.match('CrowHello')

print(m)


# ^
print(re.search('^Life', 'Life is too short'))

print(re.search('^Life', 'My Life'))


# $
print(re.search('short$', 'Life is too short'))

print(re.search('short$', 'Life is too short, you need python'))


# \A


# \Z


# \b
p = re.compile(r'\bclass\b')

print(p.search('no class at all'))

print(p.search('the declassified algorithm'))

print(p.search('one subclass is'))


# \B
p = re.compile(r'\Bclass\B')

print(p.search('no class at all'))

print(p.search('the declassified algorithm'))

print(p.search('one subclass is'))