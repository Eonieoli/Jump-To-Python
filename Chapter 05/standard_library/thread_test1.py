import time

def long_task():                    # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)               # 1초 대기
        print("working: %s\n" % i)

print("Start")
for i in range(5):
    long_task()

print("End")