# 여러 줄인 문자열을 변수에 대입하고 싶을 때

## 1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"
print(multiline)

# 2. 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기
multiline = '''
Life is too short
You need python
'''
print(multiline)
multiline = """
Life is too short
You need python
"""
print(multiline)