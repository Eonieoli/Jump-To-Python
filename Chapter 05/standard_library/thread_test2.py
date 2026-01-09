import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" % i)

print("Start")

threads = []
for i in range(5):
    # long_task()
    t = threading.Thread(target=long_task)      # 스레드를 생성
    threads.append(t)

for t in threads:
    t.start()                                   # 스레드를 실행

print("End")