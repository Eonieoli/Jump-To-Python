try:
    f = open("foo.txt", 'w', encoding='utf-8')
    # 무언가를 수행
finally:
    f.close()   # 중간에 오류가 발생하더라도 부조건 실행