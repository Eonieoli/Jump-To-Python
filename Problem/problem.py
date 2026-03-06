# 1
# text = "a:b:c:d"
# splited = text.split(":")
# joined = "#".join(splited)
# print(joined)


# 2
# a = {'A': 90, 'B': 80}
# print(a.get('C', 70))


# 3
# a = [1, 2, 3]
# print(a)
# print(id(a))
# a = a + [4, 5]
# print(a)
# print(id(a))
# # + 연산은 새로운 리스트를 생성해서 a에 재할당하는 것이므로 id가 바뀐다.

# a = [1, 2, 3]
# print(a)
# print(id(a))
# a.extend([4, 5])
# print(a)
# print(id(a))
# # extend 메서드는 기존 리스트를 수정하는 것이므로 id가 바뀌지 않는다.


# 4
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

# total = 0
# for score in A:
#     if score >= 50:
#         total += score
# print(total)


# 5
# def fibonacci(n: int) -> None:
#     num1 = 0
#     num2 = 1
#     if n <= 0:
#         pass
#     elif n == 1:
#         print(num1)
#         return
#     elif n == 2:
#         print(f"{num1}, {num2}")
#     else:
#         print(f"{num1}, {num2}, ", end='')
#         for i in range(3, n):
#             num3 = num1 + num2
#             print(f"{num3}, ", end='')
#             num1 = num2
#             num2 = num3
#         print(num1+num2)
#     return

# fibonacci(10)


# 6
# numbers_str = input("','로 구분된 숫자들을 입력하세요.")
# numbers_list = numbers_str.split(",")

# total = 0
# for number in numbers_list:
#     total += int(number)
# print(total)


# 7
# dan = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
# for i in range(1, 9):
#     print(dan * i, end=' ')
# print(dan * 9)


# 8
# f = open('abc.txt', 'r')
# lines = f.readlines()
# f.close()

# lines.reverse()

# f = open('abc.txt', 'w')
# for line in lines:
#     line = line.strip()
#     f.write(line)
#     f.write('\n')
# f.close()


# 9
# f = open('sample.txt', 'r')
# lines = f.readlines()
# f.close()

# total = 0
# cnt = len(lines)
# for line in lines:
#     total += int(line.strip())
# average = total / len(lines)

# f = open('result.txt', 'w')
# f.write(str(average))
# f.close()


# 10
# from typing import List

# class Calculator:
#     def __init__(self, numbers: List[int] = []):
#         self.numbers = numbers
    
#     def sum(self) -> int:
#         return sum(self.numbers)
    
#     def avg(self) -> float:
#         return sum(self.numbers) / len(self.numbers)
    
# cal1 = Calculator([1, 2, 3, 4, 5])
# print(cal1.sum())
# print(cal1.avg())

# cal2 = Calculator([6, 7, 8, 9, 10])
# print(cal2.sum())
# print(cal2.avg())


# 11
# 1. sys 모듈 사용하기
# import sys
# sys.path.append("c:/doit")
# import mymod

# 2. PYTHONPATH 환경 변수 사용하기
# C:\Users\home>set PYTHONPATH=c:\doit
# C:\Users\home>python
# import mymod

# 3. 현재 디렉토리 사용하기
# C:\Users\home>cd c:\doit
# C:\doit>python
# import mymod


# 12
# result = 0

# try:
#     [1, 2, 3][3]
#     "a" + 1
#     4 / 0
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result += 2
# except IndexError:
#     result += 3
# finally:
#     result += 4

# print(result)
# # 7: 처음 만나는 에러가 IndexError이고, 다음 코드는 넘어간 후 finally로 넘어간다.


# 13
# def DashInsert(num_str: str) -> str:
#     new_str = ''
#     for i in range(len(num_str)-1):
#         new_str += num_str[i]

#         is_odd = int(num_str[i]) % 2
#         will_odd = int(num_str[i+1]) % 2

#         if is_odd and will_odd:
#             new_str += '-'
#         elif (is_odd == 0) and (will_odd == 0):
#             new_str += '*'
#     new_str += num_str[-1]
#     return new_str

# print(DashInsert('4546793'))


# 14
# def compress(text: str) -> str:
#     new_str = ''
#     i = 0
#     while i < len(text):
#         new_str += text[i]
#         cnt = 1
#         j = i + 1
#         while j < len(text) and text[j] == text[i]:
#             j += 1
#             cnt += 1
#         new_str += str(cnt)
#         i = j
#     return new_str

# print(compress('aaabbcccccca'))


# 15
# def duplicate_numbers(numbers: str) -> str:
#     number_count = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
#                     '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
#     for i in range(len(numbers)):
#         number_count[numbers[i]] += 1
    
#     for count in number_count.values():
#         if count != 1:
#             return False
#     return True

# print(duplicate_numbers('0123456789'))
# print(duplicate_numbers('01234'))
# print(duplicate_numbers('01234567890'))
# print(duplicate_numbers('6789012345'))
# print(duplicate_numbers('012322456789'))


# 16
# def decode_morse(code: str) -> str:
#     decoder = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
#                '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
#                '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
#                '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
#                '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
#                '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
#                '-.--': 'Y', '--..': 'Z', '': ' '}
    
#     decoded = ''
#     code_list = code.split(' ')
#     for i in range(len(code_list)):
#         decoded += decoder[code_list[i]]
#     return decoded

# print(decode_morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))


# 17
# import re

# pattern = re.compile(r"a[.]{3,}b")
# print(pattern.match("acccb"))
# print(pattern.match("a....b"))
# print(pattern.match("aaab"))
# print(pattern.match("a.cccb"))
# 2


# 18
import re

p = re.compile("[a-z]+")
m = p.search("5 python")
print(m.start() + m.end())
# 2 + 8 = 10


# 19
import re

text = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pattern = re.compile(r"\w+\s\d+[-]\d+[-](\d+)")
pattern.sub("\g<1>")