# Before

# total1  =  0

# for i in range(0,100000000):
#     total1 += i
# print(total1)


# After

from threading import Thread
def calc(start,end):
    total = 0
    for i in range(start,end):
        total += i
    print(total)

if __name__ == "__main__":
    start, end = 0, 100000000
    thr1 = Thread(target=calc,args=(start,end))

    thr1.start()
    thr1.join()

# cpu가 4개있는데 문제를 같이 해결 => 멀티스레드

# cpu가 4개있는데 문제를 각자에게 주어 각각 해결 => 멀티프로세스