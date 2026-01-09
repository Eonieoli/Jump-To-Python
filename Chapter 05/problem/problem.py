# 1
class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)


# 2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        # self.value = 100 if self.value + val >=100 else self.value + val
        if self.value + val >= 100:
            self.value = 100
        else:
            self.value += val

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)


# 3
print(all([1, 2, abs(-3)-3]))
print(chr(ord('a')) == 'a')


# 4
print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))


# 5
print(int(0xea))


# 6
print(list(map(lambda x: x * 3, [1, 2, 3, 4])))


# 7
a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a) + min(a))


# 8
print(round(17/3, 4))


# 9
import os
os.chdir("C:/Users/user/Desktop/김재혁/Code/Jump To Python")
f = os.popen("dir")
print(f.read())
f.close()


# 10 ##########
import glob
print(glob.glob("./*.py"))


# 11
import time
print(time.strftime('%y/%m/%d %H:%M:%S', time.localtime(time.time())))


# 12
import random
print(random.sample(range(1, 46), 6))


# 13
import datetime
day1 = datetime.date(1995, 11, 20)
day2 = datetime.date(1998, 10, 6)
diff = day2 - day1
print(diff.days)


# 14
from operator import itemgetter
data = [
    ('윤서현', 15.25),
    ('김예지', 13.31),
    ('박예원', 15.34),
    ('송순자', 15.57),
    ('김시우', 15.48),
    ('배숙자', 17.9),
    ('전정웅', 13.39),
    ('김혜진', 16.63),
    ('최보람', 17.14),
    ('한지영', 14.83),
    ('이성호', 17.7),
    ('김옥순', 16.71),
    ('황민지', 17.65),
    ('김영철', 16.7),
    ('주병철', 15.67),
    ('박상현', 14.16),
    ('김영순', 14.81),
    ('오지아', 15.13),
    ('윤지은', 16.93),
    ('문재호', 16.39)
]
result = sorted(data, key=itemgetter(1))
print(result)


# 15
import itertools
print(list(itertools.combinations(['나지혜', '성성민', '윤지현', '김정숙'], 2)))


# 16
result = list(itertools.permutations("abcd"))
result_str = list(map(''.join, result))
for i in range(len(result_str)):
    print(f'{result_str[i]},', end=' ')
print(result_str[-1])


# 17
people = ['김승현', '김진호', '강춘자', '이예준', '김현주']
works = ['청소', '빨래', '설거지']

people = random.sample(people, len(people))
print(list(itertools.zip_longest(people, works, fillvalue='휴식')))


# 18
import math
print(math.gcd(200, 80))